---
title: About
menu:
    main: 
        weight: 1
        params:
            icon: home

comments: false
---

<style>
.resume-container {
    max-width: 1100px;
    margin: 0 auto;
    font-family: inherit;
    font-size: 1.2rem;
}

.resume-section {
    margin-bottom: 3rem;
    border-radius: 18px;
    padding: 2.5rem;
    box-shadow: 0 4px 20px rgba(0,0,0,0.08);
    backdrop-filter: blur(12px);
}

.resume-section.traits {
    background: rgba(254, 243, 199, 0.65);
    border: 1px solid rgba(253, 230, 138, 0.5);
}

.resume-section.education {
    background: rgba(219, 234, 254, 0.65);
    border: 1px solid rgba(191, 219, 254, 0.5);
}

.resume-section.projects {
    background: rgba(220, 252, 231, 0.65);
    border: 1px solid rgba(187, 247, 208, 0.5);
}

.resume-section.skills {
    background: rgba(243, 232, 255, 0.65);
    border: 1px solid rgba(233, 213, 255, 0.5);
}

[data-scheme="dark"] .resume-section.traits {
    background: rgba(120, 53, 15, 0.2);
    border: 1px solid rgba(180, 83, 9, 0.3);
}

[data-scheme="dark"] .resume-section.education {
    background: rgba(30, 64, 175, 0.2);
    border: 1px solid rgba(59, 130, 246, 0.3);
}

[data-scheme="dark"] .resume-section.projects {
    background: rgba(22, 101, 52, 0.2);
    border: 1px solid rgba(34, 197, 94, 0.3);
}

[data-scheme="dark"] .resume-section.skills {
    background: rgba(88, 28, 135, 0.2);
    border: 1px solid rgba(147, 51, 234, 0.3);
}

.section-title {
    font-size: 2rem;
    font-weight: 700;
    color: var(--accent-color, #2563eb);
    margin-bottom: 2rem;
}

/* 个人特质 */
.traits-container {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
    gap: 1.25rem;
}

.trait-card {
    background: rgba(255, 255, 255, 0.85);
    border-radius: 16px;
    padding: 1.75rem;
    box-shadow: 0 2px 12px rgba(0,0,0,0.06);
    transition: transform 0.2s, box-shadow 0.2s;
    backdrop-filter: blur(10px);
}

[data-scheme="dark"] .trait-card {
    background: rgba(30, 30, 30, 0.7);
}

.trait-card:hover {
    transform: translateY(-4px);
    box-shadow: 0 6px 20px rgba(0,0,0,0.12);
}

.trait-icon {
    font-size: 2.8rem;
    margin-bottom: 0.85rem;
}

.trait-title {
    font-weight: 600;
    font-size: 1.4rem;
    margin-bottom: 0.5rem;
}

.trait-desc {
    font-size: 1.1rem;
    color: var(--body-text-color, #64748b);
    line-height: 1.6;
}

/* 学习经历时间线 */
.timeline {
    position: relative;
    padding-left: 40px;
}

.timeline::before {
    content: '';
    position: absolute;
    left: 11px;
    top: 0;
    bottom: 0;
    width: 5px;
    background: linear-gradient(180deg, var(--accent-color, #2563eb) 0%, #60a5fa 100%);
    border-radius: 5px;
}

.timeline-item {
    position: relative;
    padding-bottom: 3rem;
}

.timeline-item:last-child {
    padding-bottom: 0;
}

.timeline-dot {
    position: absolute;
    left: -34px;
    top: 5px;
    width: 20px;
    height: 20px;
    background: var(--accent-color, #2563eb);
    border-radius: 50%;
    border: 4px solid rgba(255, 255, 255, 0.9);
    box-shadow: 0 0 0 4px var(--accent-color, #2563eb);
}

[data-scheme="dark"] .timeline-dot {
    border-color: rgba(30, 30, 30, 0.9);
}

.timeline-date {
    font-size: 1.1rem;
    color: var(--accent-color, #2563eb);
    font-weight: 600;
    margin-bottom: 0.5rem;
}

.timeline-title {
    font-size: 1.5rem;
    font-weight: 700;
    margin-bottom: 0.5rem;
}

.timeline-subtitle {
    font-size: 1.2rem;
    color: var(--body-text-color, #64748b);
    margin-bottom: 0.5rem;
}

.timeline-desc {
    font-size: 1.1rem;
    color: var(--body-text-color, #64748b);
}

/* 项目经历 */
.projects-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 1.75rem;
}

.project-card {
    background: rgba(255, 255, 255, 0.85);
    border-radius: 16px;
    padding: 2rem;
    box-shadow: 0 2px 12px rgba(0,0,0,0.06);
    transition: transform 0.2s, box-shadow 0.2s;
    border-left: 5px solid var(--accent-color, #2563eb);
    backdrop-filter: blur(10px);
}

[data-scheme="dark"] .project-card {
    background: rgba(30, 30, 30, 0.7);
}

.project-card:hover {
    transform: translateY(-4px);
    box-shadow: 0 6px 20px rgba(0,0,0,0.12);
}

.project-title {
    font-size: 1.5rem;
    font-weight: 700;
    margin-bottom: 0.7rem;
}

.project-tags {
    display: flex;
    flex-wrap: wrap;
    gap: 0.6rem;
    margin-bottom: 1rem;
}

.project-tag {
    font-size: 1rem;
    background: rgba(37, 99, 235, 0.1);
    color: var(--accent-color, #2563eb);
    padding: 0.35rem 0.9rem;
    border-radius: 20px;
}

.project-desc {
    font-size: 1.1rem;
    color: var(--body-text-color, #64748b);
    line-height: 1.7;
}

.project-link {
    display: inline-flex;
    align-items: center;
    margin-top: 1.2rem;
    font-size: 1.1rem;
    color: var(--accent-color, #2563eb);
    text-decoration: none;
    font-weight: 500;
}

.project-link:hover {
    text-decoration: underline;
}

/* 技术栈 */
.skills-container {
    display: flex;
    flex-direction: column;
    gap: 1.75rem;
}

.skill-category {
    margin-bottom: 0.5rem;
}

.skill-category-title {
    font-weight: 600;
    font-size: 1.3rem;
    margin-bottom: 1.2rem;
    color: var(--body-text-color, #334155);
}

.skill-tags {
    display: flex;
    flex-wrap: wrap;
    gap: 1rem;
}

.skill-tag {
    display: inline-flex;
    align-items: center;
    gap: 0.6rem;
    background: rgba(255, 255, 255, 0.85);
    padding: 0.75rem 1.4rem;
    border-radius: 12px;
    font-size: 1.1rem;
    box-shadow: 0 2px 8px rgba(0,0,0,0.06);
    transition: transform 0.2s, box-shadow 0.2s;
    backdrop-filter: blur(10px);
}

[data-scheme="dark"] .skill-tag {
    background: rgba(30, 30, 30, 0.7);
}

.skill-tag:hover {
    transform: translateY(-3px);
    box-shadow: 0 6px 12px rgba(0,0,0,0.1);
}

.skill-level {
    width: 12px;
    height: 12px;
    border-radius: 50%;
}

.level-expert { background: #10b981; }
.level-advanced { background: #3b82f6; }
.level-intermediate { background: #f59e0b; }
</style>

<div class="resume-container">

<!-- 个人特质 -->
<section class="resume-section traits">
<h2 class="section-title">🎯 个人特质</h2>
<div class="traits-container">
    <div class="trait-card">
        <div class="trait-icon">💡</div>
        <div class="trait-title">创新思维</div>
        <div class="trait-desc">善于发现问题并提出创新解决方案，具有较强的独立思考能力</div>
    </div>
    <div class="trait-card">
        <div class="trait-icon">🤝</div>
        <div class="trait-title">团队协作</div>
        <div class="trait-desc">优秀的沟通协调能力，能够与团队成员高效配合完成项目</div>
    </div>
    <div class="trait-card">
        <div class="trait-icon">📚</div>
        <div class="trait-title">持续学习</div>
        <div class="trait-desc">对新技术保持热情，主动学习前沿知识并应用于实践</div>
    </div>
    <div class="trait-card">
        <div class="trait-icon">⚡</div>
        <div class="trait-title">执行力强</div>
        <div class="trait-desc">目标导向，能够高效推进项目进度，按时交付高质量成果</div>
    </div>
</div>
</section>

<!-- 学习经历 -->
<section class="resume-section education">
<h2 class="section-title">🎓 学习经历</h2>
<div class="timeline">
    <div class="timeline-item">
        <div class="timeline-dot"></div>
        <div class="timeline-date">2024.09 - 至今</div>
        <div class="timeline-title">哈尔滨工业大学</div>
        <div class="timeline-subtitle">人工智能专业 · 本科</div>
        <div class="timeline-desc"></div>
    </div>
    <div class="timeline-item">
        <div class="timeline-dot"></div>
        <div class="timeline-date">2021.09 - 2024.06</div>
        <div class="timeline-title">汕头市潮阳实验学校</div>
        <div class="timeline-subtitle">理科方向</div>
        <div class="timeline-desc">信息竞赛二等奖</div>
    </div>
    <div class="timeline-item">
        <div class="timeline-dot"></div>
        <div class="timeline-date">2018.09 - 2021.06</div>
        <div class="timeline-title">汕头市潮阳实验初中</div>
    </div>
</div>
</section>

<!-- 项目经历 -->
<section class="resume-section projects">
<h2 class="section-title">💼 项目经历</h2>
<div class="projects-grid">
    <div class="project-card">
        <div class="project-title">无人机机械臂远程抓取控制</div>
        <div class="project-tags">
            <span class="project-tag">Python</span>
            <span class="project-tag">Arduino</span>
            <span class="project-tag">舵机控制</span>
        </div>
        <div class="project-desc">构建地面站，远程控制机上机械臂抓取物品。团队作品获CADC国家一等奖。</div>
    </div>
    <div class="project-card">
        <div class="project-title">在线英文语音ai评测</div>
        <div class="project-tags">
            <span class="project-tag">go</span>
            <span class="project-tag">nginx</span>
            <span class="project-tag">WebSocket</span>
        </div>
        <div class="project-desc">前后端搭建完整web，配置和部署讯飞API，实时评测用户提供的语音。</div>
        <a href="#" class="project-link">查看项目 →</a>
    </div>
    <div class="project-card">
        <div class="project-title">个人博客系统</div>
        <div class="project-tags">
            <span class="project-tag">Hugo</span>
            <span class="project-tag">Go</span>
            <span class="project-tag">GitHub Pages</span>
        </div>
        <div class="project-desc">基于 Hugo 静态站点生成器搭建的个人博客，支持 Markdown 写作、代码高亮、暗黑模式等功能。</div>
        <a href="https://github.com/Ceritor-Hanio/Ceritor-Hanio.github.io" class="project-link">查看项目 →</a>
    </div>
</div>
</section>

<!-- 技术栈 -->
<section class="resume-section skills">
<h2 class="section-title">🛠️ 技术栈</h2>
<div class="skills-container">
    <div class="skill-category">
        <div class="skill-category-title">编程语言</div>
        <div class="skill-tags">
            <span class="skill-tag"><span class="skill-level level-expert"></span>JavaScript</span>
            <span class="skill-tag"><span class="skill-level level-expert"></span>TypeScript</span>
            <span class="skill-tag"><span class="skill-level level-advanced"></span>Python</span>
            <span class="skill-tag"><span class="skill-level level-advanced"></span>Go</span>
            <span class="skill-tag"><span class="skill-level level-intermediate"></span>Java</span>
        </div>
    </div>
    <div class="skill-category">
        <div class="skill-category-title">前端技术</div>
        <div class="skill-tags">
            <span class="skill-tag"><span class="skill-level level-expert"></span>React</span>
            <span class="skill-tag"><span class="skill-level level-expert"></span>Vue</span>
            <span class="skill-tag"><span class="skill-level level-advanced"></span>Next.js</span>
            <span class="skill-tag"><span class="skill-level level-advanced"></span>Tailwind CSS</span>
        </div>
    </div>
    <div class="skill-category">
        <div class="skill-category-title">后端 & 数据库</div>
        <div class="skill-tags">
            <span class="skill-tag"><span class="skill-level level-advanced"></span>Node.js</span>
            <span class="skill-tag"><span class="skill-level level-advanced"></span>MySQL</span>
            <span class="skill-tag"><span class="skill-level level-intermediate"></span>Redis</span>
        </div>
    </div>
    <div class="skill-category">
        <div class="skill-category-title">工具 & 其他</div>
        <div class="skill-tags">
            <span class="skill-tag"><span class="skill-level level-expert"></span>Git</span>
            <span class="skill-tag"><span class="skill-level level-advanced"></span>Docker</span>
            <span class="skill-tag"><span class="skill-level level-advanced"></span>Linux</span>
        </div>
    </div>
</div>
<p style="font-size: 0.95rem; color: var(--body-text-color, #64748b); margin-top: 1.25rem;">
    <span class="skill-level level-expert" style="display: inline-block; margin-right: 5px;"></span> 精通 &nbsp;&nbsp;
    <span class="skill-level level-advanced" style="display: inline-block; margin-right: 5px;"></span> 熟练 &nbsp;&nbsp;
    <span class="skill-level level-intermediate" style="display: inline-block; margin-right: 5px;"></span> 掌握
</p>
</section>

</div>

