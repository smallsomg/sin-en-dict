#!/usr/bin/env python3
"""
僧伽罗语-英语词典数据分割工具

将 dictionary.json 按字母顺序分成4个JS文件：
- dictionary_data_1.js: A-C
- dictionary_data_2.js: D-H
- dictionary_data_3.js: I-P
- dictionary_data_4.js: Q-Z + 其他
"""

import json
import os

def main():
    # 读取原始数据
    print("读取 dictionary.json...")
    with open('/workspace/dictionary.json', 'r', encoding='utf-8-sig') as f:
        data = json.load(f)
    
    total = len(data)
    print(f"总条目数: {total}")
    
    # 按首字母分组（分成4组，每组约5-6MB）
    groups = {
        'A-C': [],      # A, B, C
        'D-H': [],      # D, E, F, G, H
        'I-P': [],      # I, J, K, L, M, N, O, P
        'Q-Z': [],      # Q, R, S, T, U, V, W, X, Y, Z, 其他
    }
    
    letters_1 = set('abc')
    letters_2 = set('defgh')
    letters_3 = set('ijklmnop')
    letters_4 = set('qrstuvwxyz')
    
    for item in data:
        en = item.get('english', item.get('en', '')).lower().strip()
        if en:
            first_char = en[0]
            if first_char in letters_1:
                groups['A-C'].append(item)
            elif first_char in letters_2:
                groups['D-H'].append(item)
            elif first_char in letters_3:
                groups['I-P'].append(item)
            else:
                groups['Q-Z'].append(item)
        else:
            groups['Q-Z'].append(item)
    
    print(f"\n分组结果:")
    print(f"  A-C: {len(groups['A-C'])} 条")
    print(f"  D-H: {len(groups['D-H'])} 条")
    print(f"  I-P: {len(groups['I-P'])} 条")
    print(f"  Q-Z: {len(groups['Q-Z'])} 条")
    
    # 生成4个JS文件
    output_dir = '/workspace'
    
    for i, (name, items) in enumerate(groups.items(), 1):
        filename = f'dictionary_data_{i}.js'
        filepath = os.path.join(output_dir, filename)
        
        # 转换字段名
        converted = []
        for item in items:
            converted.append({
                "en": item.get('english', item.get('en', '')),
                "si": item.get('sinhala', item.get('si', '')),
                "type": item.get('prefix', item.get('type', ''))
            })
        
        # 生成JS内容
        js_content = f"""// 僧伽罗语-英语词典数据 - 第{i}部分 ({name})
// 条目数: {len(converted)}
// 字母范围: {name}
const DICTIONARY_DATA_{i} = {json.dumps(converted, ensure_ascii=False, indent=0)};
"""
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(js_content)
        
        file_size = os.path.getsize(filepath) / (1024 * 1024)
        print(f"\n生成: {filename}")
        print(f"  大小: {file_size:.2f} MB")
        print(f"  条目: {len(converted)}")
    
    print("\n" + "="*50)
    print("分割完成！")
    print("="*50)

if __name__ == '__main__':
    main()
