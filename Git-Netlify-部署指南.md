好的，我帮你把整个操作过程整理成了一份清晰的文档。你可以把它保存为 `Git-Netlify-部署指南.md`，方便以后查阅。

---

# Git 与 Netlify 部署完整指南

> 本文档记录了从本地项目到 GitHub，再到 Netlify 自动部署的完整流程，包括常见问题和解决方案。

## 一、基础概念

| 命令/概念 | 说明 |
|----------|------|
| `git init` | 初始化本地仓库，让 Git 开始管理这个文件夹 |
| `git add .` | 添加所有变化（新增、修改、删除）到暂存区 |
| `git commit -m "说明"` | 提交，给这次变化拍个快照 |
| `git push` | 推送到 GitHub 远程仓库 |
| `origin` | GitHub 远程仓库的默认别名 |
| `main` | 主分支名（GitHub 默认） |

---

## 二、完整操作流程

### 第一步：进入项目文件夹

```bash
cd "你的项目文件夹路径"
```

> 路径有空格时，需要用双引号包裹。

### 第二步：初始化 Git 仓库

```bash
git init
```

执行成功会显示：
```
Initialized empty Git repository in 你的路径/.git/
```

### 第三步：添加所有文件

```bash
git add .
```

> 可能会出现 `LF will be replaced by CRLF` 的警告，这是 Windows 系统的换行符提示，**可以忽略**，不影响功能。

### 第四步：配置用户信息（首次使用时）

```bash
git config --global user.email "你的邮箱@example.com"
git config --global user.name "你的用户名"
```

> 只需要配置一次，这台电脑上所有 Git 仓库都会使用这个身份。

### 第五步：提交第一个版本

```bash
git commit -m "首次提交"
```

### 第六步：连接 GitHub 远程仓库

先在 GitHub 网站上创建仓库（**不要勾选** README、.gitignore 等文件），然后：

```bash
git remote add origin https://github.com/你的用户名/仓库名.git
```

### 第七步：重命名主分支并推送

```bash
git branch -M main
git push -u origin main
```

> `-u` 会建立本地分支与远程分支的关联，之后只需要 `git push` 即可。

---

## 三、常见问题及解决方案

### 问题 1：`fatal: not a git repository`

**原因**：当前目录没有初始化 Git 仓库。

**解决**：
```bash
git init
```

---

### 问题 2：`Author identity unknown`

**原因**：没有配置用户信息。

**解决**：
```bash
git config --global user.email "你的邮箱"
git config --global user.name "你的用户名"
```

---

### 问题 3：`No configured push destination`

**原因**：没有添加远程仓库地址。

**解决**：
```bash
git remote add origin https://github.com/用户名/仓库名.git
```

---

### 问题 4：`[rejected] main -> main (fetch first)`

**原因**：GitHub 仓库里有文件（如 README.md），但本地没有。

**解决一（合并）**：
```bash
git pull origin main --allow-unrelated-histories
git push -u origin main
```

**解决二（强制覆盖）**：
```bash
git push -u origin main --force
```
> ⚠️ 强制覆盖会删除 GitHub 上原有的文件，只保留本地的。

---

### 问题 5：`Failed to connect to github.com port 443`

**原因**：代理问题或网络连接问题。

**解决一（设置代理）**：
```bash
git config --global http.proxy http://127.0.0.1:你的代理端口
git config --global https.proxy http://127.0.0.1:你的代理端口
```

常见代理端口：Clash（7890）、V2Ray（10809）、SSR（1080）

**解决二（取消代理）**：
```bash
git config --global --unset http.proxy
git config --global --unset https.proxy
```

**解决三（改用 SSH）**：
```bash
# 修改远程地址为 SSH 格式
git remote set-url origin git@github.com:用户名/仓库名.git

# 测试连接
ssh -T git@github.com
```

---

### 问题 6：Netlify 部署后出现 404

**原因**：网站根目录下没有 `index.html` 文件。

**解决**：
1. 把主 HTML 文件重命名为 `index.html`
2. 提交并推送：
```bash
git add .
git commit -m "添加index.html作为首页"
git push
```
3. 等待 30 秒，重新访问你的 Netlify 网址

---

## 四、日常更新流程（部署新版本）

当你需要更新网站时，只需要执行这三条命令：

```bash
git add .
git commit -m "更新说明"
git push
```

> 执行 `git push` 后，Netlify 会自动检测到更新并重新部署网站，约 10-30 秒生效。

---

## 五、常用命令速查

| 命令 | 作用 |
|------|------|
| `git status` | 查看当前状态（哪些文件被修改了） |
| `git add .` | 添加所有变化 |
| `git add 文件名` | 只添加指定文件 |
| `git commit -m "说明"` | 提交 |
| `git push` | 推送到 GitHub |
| `git pull` | 从 GitHub 拉取最新代码 |
| `git log` | 查看提交历史 |
| `git remote -v` | 查看远程仓库地址 |

---

## 六、文件记录

本次操作涉及的项目：
- **本地路径**：`D:\jsyanta\Trae test\sin-en dict\workspace`
- **GitHub 仓库**：`https://github.com/smallsomg/sin-en-dict.git`
- **Netlify 网址**：`https://sin-en-dict.netlify.app`

提交历史：
| Commit ID | 说明 |
|-----------|------|
| `885d9d5` | 首次提交（11个文件） |
| `657c94e` | 添加 index.html 作为首页 |

---

*文档生成时间：2026年5月27日*