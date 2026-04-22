# 仓库重构与优化建议

## 当前主要问题

1. 目录语义不统一（如 `mathemathics` 拼写、`src` 目录用途模糊）。
2. 资源文件命名混杂（中文、空格、括号并存），不利于长期维护与自动化处理。
3. 页面普遍使用内联样式，公共样式和结构复用不足。
4. 大体积媒体资源直接入仓，仓库增长过快，协作和发布成本高。

## 建议的目标目录结构

```text
.
├── index.html
├── assets/
│   ├── site/           # 站点通用资源（logo、背景、图标）
│   ├── blog/           # 博客图片/视频等
│   └── video/          # 视频专区媒体
├── blog/               # 博客页面
├── algorithm/          # 算法相关页面/素材
├── mathematics/        # 数学页面（统一拼写）
├── genshin/            # 独立主题页面
├── WebGL-CW/           # 课程项目
└── video/              # 视频页面
```

## 已完成重构（本次）

1. `mathemathics/` 重命名为 `mathematics/`。
2. `blog/src/` 重命名为 `blog/assets/`，并修复 `blog/daily.html` 中相关引用。
3. `video/src/` 重命名为 `video/assets/`，并修复 `video/index.html` 中相关引用。
4. 修复主页中的数学链接：`./mathematics/index.html`。
5. 删除仓库中的 `.DS_Store`，并在 `.gitignore` 中加入忽略规则。
6. 处理 `video/assets/ 云中探花手.mp4` 的前导空格命名问题。

## 下一步建议（可分阶段）

1. 将页面中的内联 CSS 提取到公共样式文件（如 `assets/site/base.css`）。
2. 统一文件命名规范为 `kebab-case`（避免空格、括号和混合命名）。
3. 建立内容索引（文章/视频元数据）并由脚本生成列表页，减少手工维护。
4. 将大体积媒体迁移到对象存储 + CDN（仓库仅保留必要缩略图和页面源码）。
5. 引入轻后端（Serverless + 数据库）实现评论、统计、搜索等动态能力。

## 后端接入建议（从轻到重）

1. **轻量起步**：GitHub Pages + Cloudflare Workers/Vercel Functions + Supabase。  
   适合评论、点赞、访问统计、搜索索引。
2. **中等方案**：Astro/Next.js + Supabase。  
   增强内容管理、标签检索、后台录入。
3. **完整方案**：Next.js + NestJS + Postgres + 对象存储。  
   支持账号体系、权限、私密内容与更复杂业务。
