# 仓库重构与优化建议

## 当前主要问题

1. 目录语义不统一（如 `mathemathics` 拼写、`src` 目录用途模糊）。
2. 资源文件命名混杂（中文、空格、括号并存），不利于长期维护与自动化处理。
3. 页面普遍使用内联样式，公共样式和结构复用不足。
4. 大体积媒体资源直接入仓，仓库增长过快，协作和发布成本高。

## 建议的目标目录结构

```text
.
├── index.html (redirect)
├── texas.html (redirect)
├── pages/
│   ├── home/index.html
│   └── texas/index.html
├── assets/
│   └── site/
│       ├── media/      # 站点通用资源（logo、背景、图标）
│       └── pages/      # 页面样式
├── blog/               # 博客页面
│   └── assets/
│       ├── images/
│       └── videos/
├── algorithm/          # 算法相关页面/素材
├── mathematics/        # 数学页面（统一拼写）
├── genshin/
│   └── assets/
├── projects/
│   └── webgl-coursework/
└── video/
    └── videos/
```

## 已完成重构（本次）

1. `mathemathics/` 重命名为 `mathematics/`。
2. `blog/src/` 重命名为 `blog/assets/`，后续再拆分为 `blog/assets/images` + `blog/assets/videos`。
3. `video/src/` 重命名后进一步整理为 `video/videos/`，并修复 `video/index.html` 中相关引用。
4. `genshin` 资源收拢到 `genshin/assets/` 并修复页面引用。
5. 删除仓库中的 `.DS_Store`，并在 `.gitignore` 中加入忽略规则。
6. 处理 `video/assets/ 云中探花手.mp4` 的前导空格命名问题，并统一为 `video/videos/yunzhong-tanhuashou.mp4`。
7. `algorithm/boid-model/test.py/` 调整为 `algorithm/boid-model/scripts/`。
8. `WebGL-CW/` 迁移到 `projects/webgl-coursework/`。
9. `log/` 迁移到 `assets/site/media/`。
10. `index.html` 与 `texas.html` 归档到 `pages/`，根目录保留跳转页。

## 下一步建议（可分阶段）

1. 将更多页面继续组件化（header/footer/nav），减少重复 HTML。
2. 将大体积媒体迁移到对象存储 + CDN（仓库仅保留必要缩略图和页面源码）。
3. 引入轻后端（Serverless + 数据库）实现评论、统计、搜索等动态能力。
4. 将大体积媒体迁移到对象存储 + CDN（仓库仅保留必要缩略图和页面源码）。
5. 引入轻后端（Serverless + 数据库）实现评论、统计、搜索等动态能力。

## 后端接入建议（从轻到重）

1. **轻量起步**：GitHub Pages + Cloudflare Workers/Vercel Functions + Supabase。  
   适合评论、点赞、访问统计、搜索索引。
2. **中等方案**：Astro/Next.js + Supabase。  
   增强内容管理、标签检索、后台录入。
3. **完整方案**：Next.js + NestJS + Postgres + 对象存储。  
   支持账号体系、权限、私密内容与更复杂业务。
