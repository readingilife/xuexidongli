<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>Basic English - Ogden's 850 Words</title>
    <link rel="icon" type="image/svg+xml" href="icon/学习.svg">
    <style>
        :root {
            --c1: #FF6B6B; --c1-light: #FFF0F0;
            --c2: #4ECDC4; --c2-light: #E8FAF8;
            --c3: #45B7D1; --c3-light: #E8F7FB;
            --c4: #96CEB4; --c4-light: #F0F8F4;
            --c5: #FFEAA7; --c5-light: #FFFBF0;
            --c6: #DDA0DD; --c6-light: #FAF0FA;
            --text: #2d3436;
            --text-light: #636e72;
            --bg: #f8f9fa;
            --card: #ffffff;
            --border: #e9ecef;
            --shadow: 0 2px 12px rgba(0,0,0,0.08);
            --shadow-hover: 0 8px 30px rgba(0,0,0,0.12);
        }
        * { box-sizing: border-box; margin: 0; padding: 0; }
        html { scroll-behavior: smooth; }
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'PingFang SC', 'Hiragino Sans GB', 'Microsoft YaHei', sans-serif;
            background: var(--bg);
            color: var(--text);
            line-height: 1.6;
            -webkit-font-smoothing: antialiased;
        }

        /* ===== 顶部导航 ===== */
        .top-bar {
            position: sticky;
            top: 0;
            z-index: 100;
            background: rgba(255,255,255,0.95);
            backdrop-filter: blur(10px);
            border-bottom: 1px solid var(--border);
            padding: 12px 0;
        }
        .top-bar-inner {
            max-width: 1200px;
            margin: 0 auto;
            padding: 0 16px;
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 12px;
        }
        .logo {
            font-size: 16px;
            font-weight: 700;
            color: var(--text);
            white-space: nowrap;
            flex: 0 0 auto;
            display: flex;
            align-items: center;
            gap: 6px;
        }
        .logo-icon {
            width: 22px;
            height: 22px;
        }
        .grade-nav {
            display: flex;
            gap: 6px;
            overflow-x: auto;
            scrollbar-width: none;
            -ms-overflow-style: none;
            flex: 1;
            justify-content: center;
        }
        .back-link {
            flex: 0 0 auto;
            font-size: 13px;
            font-weight: 600;
            color: var(--text-light);
            text-decoration: none;
            padding: 6px 12px;
            border-radius: 16px;
            background: var(--bg);
            border: 1px solid var(--border);
            transition: all 0.2s;
            white-space: nowrap;
        }
        .back-link:hover {
            background: linear-gradient(135deg, #667eea, #764ba2);
            color: #fff;
            border-color: transparent;
        }
        .grade-nav::-webkit-scrollbar { display: none; }
        .grade-nav a {
            display: inline-flex;
            align-items: center;
            justify-content: center;
            min-width: 36px;
            height: 32px;
            padding: 0 10px;
            border-radius: 16px;
            font-size: 13px;
            font-weight: 600;
            text-decoration: none;
            color: var(--text-light);
            background: var(--bg);
            border: 1px solid var(--border);
            transition: all 0.2s;
            white-space: nowrap;
        }
        .grade-nav a:hover, .grade-nav a.active {
            color: #fff;
            transform: translateY(-1px);
        }
        .grade-nav a[href="#operations"]:hover, .grade-nav a[href="#operations"].active { background: var(--c1); border-color: var(--c1); }
        .grade-nav a[href="#things-general"]:hover, .grade-nav a[href="#things-general"].active { background: var(--c2); border-color: var(--c2); }
        .grade-nav a[href="#things-picturable"]:hover, .grade-nav a[href="#things-picturable"].active { background: var(--c3); border-color: var(--c3); }
        .grade-nav a[href="#qualities"]:hover, .grade-nav a[href="#qualities"].active { background: var(--c4); border-color: var(--c4); }
        .grade-nav a[href="#wordorder"]:hover, .grade-nav a[href="#wordorder"].active { background: #9b59b6; border-color: #9b59b6; }
    
        /* ===== 封面头图 ===== */
        .hero {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 48px 20px;
            text-align: center;
            position: relative;
            overflow: hidden;
        }
        .hero::before {
            content: '';
            position: absolute;
            top: -50%;
            left: -50%;
            width: 200%;
            height: 200%;
            background: radial-gradient(circle, rgba(255,255,255,0.1) 1px, transparent 1px);
            background-size: 20px 20px;
            opacity: 0.3;
        }
        .hero h1 {
            font-size: 28px;
            font-weight: 800;
            margin-bottom: 12px;
            position: relative;
            letter-spacing: -0.5px;
        }
        .hero p {
            font-size: 15px;
            opacity: 0.9;
            max-width: 500px;
            margin: 0 auto;
            position: relative;
        }
        .hero-tags {
            display: flex;
            gap: 8px;
            justify-content: center;
            margin-top: 20px;
            flex-wrap: wrap;
            position: relative;
        }
        .hero-tag {
            background: rgba(255,255,255,0.2);
            backdrop-filter: blur(4px);
            padding: 6px 14px;
            border-radius: 20px;
            font-size: 13px;
            font-weight: 500;
        }
    
        /* ===== 分类区块 ===== */
        .grade-section {
            max-width: 1200px;
            margin: 0 auto;
            padding: 40px 16px;
        }
        .grade-header {
            display: flex;
            align-items: center;
            gap: 12px;
            margin-bottom: 24px;
            padding-bottom: 16px;
            border-bottom: 3px solid;
        }
        .grade-num {
            width: 48px;
            height: 48px;
            border-radius: 14px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 22px;
            font-weight: 800;
            color: white;
            flex-shrink: 0;
            box-shadow: 0 4px 12px rgba(0,0,0,0.15);
        }
        .grade-title {
            font-size: 22px;
            font-weight: 700;
        }
        .grade-sub {
            font-size: 13px;
            color: var(--text-light);
            margin-top: 2px;
        }
    
        /* 颜色主题 */
        #operations .grade-header { border-color: var(--c1); }
        #operations .grade-num { background: var(--c1); }
        #operations .grade-title { color: var(--c1); }
        #things-general .grade-header { border-color: var(--c2); }
        #things-general .grade-num { background: var(--c2); }
        #things-general .grade-title { color: var(--c2); }
        #things-picturable .grade-header { border-color: var(--c3); }
        #things-picturable .grade-num { background: var(--c3); }
        #things-picturable .grade-title { color: var(--c3); }
        #qualities .grade-header { border-color: var(--c4); }
        #qualities .grade-num { background: var(--c4); }
        #qualities .grade-title { color: #5a9; }
        #wordorder .grade-header { border-color: #9b59b6; }
        #wordorder .grade-num { background: #9b59b6; }
        #wordorder .grade-title { color: #9b59b6; }
    
        /* ===== 单词卡片 ===== */
        .semester-grid {
            display: grid;
            grid-template-columns: 1fr;
            gap: 20px;
        }
        .semester-card {
            background: var(--card);
            border-radius: 16px;
            box-shadow: var(--shadow);
            overflow: hidden;
            transition: transform 0.2s, box-shadow 0.2s;
        }
        .semester-card:hover {
            transform: translateY(-2px);
            box-shadow: var(--shadow-hover);
        }
        .semester-header {
            padding: 16px 20px;
            display: flex;
            align-items: center;
            justify-content: space-between;
            border-bottom: 2px solid var(--border);
        }
        .semester-name {
            font-size: 17px;
            font-weight: 700;
        }
        .difficulty-badge {
            font-size: 11px;
            padding: 4px 10px;
            border-radius: 12px;
            font-weight: 600;
        }
        .difficulty-high {
            background: #ffe0e0;
            color: #c0392b;
        }
        .difficulty-medium {
            background: #fff3cd;
            color: #856404;
        }
    
        /* 分类颜色 */
        .s1 .semester-header { background: linear-gradient(90deg, var(--c1-light), transparent); border-color: var(--c1); }
        .s1 .semester-name { color: var(--c1); }
        .s2 .semester-header { background: linear-gradient(90deg, var(--c2-light), transparent); border-color: var(--c2); }
        .s2 .semester-name { color: var(--c2); }
        .s3 .semester-header { background: linear-gradient(90deg, var(--c3-light), transparent); border-color: var(--c3); }
        .s3 .semester-name { color: var(--c3); }
        .s4 .semester-header { background: linear-gradient(90deg, var(--c4-light), transparent); border-color: var(--c4); }
        .s4 .semester-name { color: #5a9; }
        .s5 .semester-header { background: linear-gradient(90deg, #f3e5f5, transparent); border-color: #9b59b6; }
        .s5 .semester-name { color: #9b59b6; }
    
        .semester-body {
            padding: 16px 20px;
        }
    
        /* ===== 单词列表 ===== */
        .word-list {
            display: flex;
            flex-wrap: wrap;
            gap: 8px;
            list-style: none;
            padding: 0;
            margin: 0;
        }
        .word-list li {
            padding: 6px 12px;
            border-radius: 8px;
            font-size: 14px;
            font-weight: 500;
            color: var(--text);
            background: var(--bg);
            border: 1px solid var(--border);
            transition: all 0.2s;
            cursor: default;
        }
        .word-list li:hover {
            transform: translateY(-1px);
            box-shadow: 0 2px 8px rgba(0,0,0,0.08);
        }
        .s1 .word-list li:hover { background: var(--c1-light); border-color: var(--c1); color: var(--c1); }
        .s2 .word-list li:hover { background: var(--c2-light); border-color: var(--c2); color: var(--c2); }
        .s3 .word-list li:hover { background: var(--c3-light); border-color: var(--c3); color: var(--c3); }
        .s4 .word-list li:hover { background: var(--c4-light); border-color: var(--c4); color: #5a9; }
        .s5 .word-list li:hover { background: #f3e5f5; border-color: #9b59b6; color: #9b59b6; }
    
        /* ===== 例句区块 ===== */
        .examples {
            display: flex;
            flex-direction: column;
            gap: 8px;
        }
        .example-item {
            padding: 10px 14px;
            border-radius: 8px;
            background: #f8f9fa;
            font-size: 14px;
            color: var(--text);
            border-left: 3px solid #9b59b6;
        }
    
        /* ===== 附录说明 ===== */
        .appendix {
            max-width: 1200px;
            margin: 0 auto;
            padding: 0 16px 40px;
        }
        .appendix-box {
            margin-top: 16px;
            padding: 16px;
            background: #f8f9fa;
            border-radius: 10px;
            font-size: 13px;
            color: var(--text-light);
            line-height: 1.8;
        }
        .appendix-box strong {
            color: var(--text);
        }
    
        /* ===== 分享条 ===== */
        .share-bar {
            position: fixed;
            bottom: 0;
            left: 0;
            right: 0;
            background: rgba(255,255,255,0.95);
            backdrop-filter: blur(10px);
            border-top: 1px solid var(--border);
            padding: 10px 16px;
            display: flex;
            justify-content: center;
            gap: 12px;
            z-index: 99;
        }
        .share-btn {
            padding: 10px 24px;
            border-radius: 24px;
            border: none;
            font-size: 14px;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.2s;
            display: flex;
            align-items: center;
            gap: 6px;
            text-decoration: none;
        }
        .share-btn.primary {
            background: linear-gradient(135deg, #667eea, #764ba2);
            color: white;
            box-shadow: 0 4px 12px rgba(102,126,234,0.3);
        }
        .share-btn.primary:hover {
            transform: translateY(-1px);
            box-shadow: 0 6px 20px rgba(102,126,234,0.4);
        }
        .share-btn.secondary {
            background: var(--bg);
            color: var(--text);
            border: 1px solid var(--border);
        }
    
        /* ===== 响应式 ===== */
        @media (max-width: 768px) {
            .hero { padding: 32px 16px; }
            .hero h1 { font-size: 22px; }
            .semester-grid { grid-template-columns: 1fr; }
            .grade-header { margin-bottom: 16px; }
            .grade-num { width: 40px; height: 40px; font-size: 18px; }
            .grade-title { font-size: 18px; }
            .grade-section { padding: 24px 12px; }
            .top-bar-inner { padding: 0 12px; }
            .grade-nav a { min-width: 32px; height: 28px; font-size: 12px; padding: 0 8px; }
            .share-btn { padding: 8px 16px; font-size: 13px; }
            body { padding-bottom: 60px; }
        }
        @media (min-width: 769px) {
            body { padding-bottom: 0; }
            .share-bar { display: none; }
        }
    
        /* 打印优化 */
        @media print {
            .top-bar, .share-bar, .hero { display: none; }
            .semester-card { break-inside: avoid; box-shadow: none; border: 1px solid #ddd; }
            .grade-section { padding: 20px 0; }
            .word-info { display: none; }
        }
        
        /* 单词卡片样式 */
        .word-list li {
            cursor: pointer;
            position: relative;
            transition: all 0.2s;
        }
        .word-list li:hover {
            transform: translateY(-2px);
            box-shadow: 0 4px 12px rgba(0,0,0,0.15);
        }
        
        /* 信息卡片 */
        .word-info {
            position: fixed;
            z-index: 1000;
            background: white;
            border-radius: 12px;
            box-shadow: 0 8px 30px rgba(0,0,0,0.2);
            padding: 16px 20px;
            max-width: 300px;
            pointer-events: none;
            opacity: 0;
            transition: opacity 0.2s;
        }
        .word-info.show {
            opacity: 1;
            pointer-events: auto;
        }
        .word-info-word {
            font-size: 24px;
            font-weight: 700;
            color: #667eea;
            margin-bottom: 8px;
        }
        .word-info-phonetic {
            font-size: 16px;
            color: #636e72;
            margin-bottom: 8px;
            font-family: 'Lucida Sans Unicode', 'Arial Unicode MS', sans-serif;
        }
        .word-info-meaning {
            font-size: 16px;
            color: #2d3436;
            line-height: 1.5;
        }
        .word-info-hint {
            font-size: 12px;
            color: #b2bec3;
            margin-top: 12px;
            padding-top: 12px;
            border-top: 1px solid #e9ecef;
        }
    </style>
</head>
<body>

<!-- 顶部导航 -->
<nav class="top-bar">
    <div class="top-bar-inner">
        <div class="logo"><img src="icon/学习.svg" class="logo-icon" alt="">Basic English</div>
        <div class="grade-nav">
            <a href="#operations" onclick="setActive(this)">Operations</a>
            <a href="#things-general" onclick="setActive(this)">Things General</a>
            <a href="#things-picturable" onclick="setActive(this)">Things Picturable</a>
            <a href="#qualities" onclick="setActive(this)">Qualities</a>
            <a href="#wordorder" onclick="setActive(this)">Word Order</a>
        </div>
        <a href="index.html" class="back-link">← 返回</a>
    </div>
</nav>

<!-- 封面 -->
<header class="hero">
    <h1>Basic English<br>Ogden's 850 Core Words</h1>
    <p>C.K. Ogden (1930) 设计的 850 个核心词汇，覆盖牛津袖珍英语词典 90% 的概念</p>
    <div class="hero-tags">
        <span class="hero-tag">850 Words</span>
        <span class="hero-tag">5 Categories</span>
        <span class="hero-tag">可打印版</span>
    </div>
</header>

<!-- Operations -->
<section class="grade-section" id="operations">
    <div class="grade-header">
        <div class="grade-num">1</div>
        <div>
            <div class="grade-title">Operations</div>
            <div class="grade-sub">100 个操作类词汇 · 动词、介词、代词、连词、副词等</div>
        </div>
    </div>
    <div class="semester-grid">
        <div class="semester-card s1">
            <div class="semester-header">
                <span class="semester-name">Operations</span>
                <span class="difficulty-badge difficulty-medium">100 words</span>
            </div>
            <div class="semester-body">
                <ul class="word-list">
                    <li>come</li>
                    <li>get</li>
                    <li>give</li>
                    <li>go</li>
                    <li>keep</li>
                    <li>let</li>
                    <li>make</li>
                    <li>put</li>
                    <li>seem</li>
                    <li>take</li>
                    <li>be</li>
                    <li>do</li>
                    <li>have</li>
                    <li>say</li>
                    <li>see</li>
                    <li>send</li>
                    <li>may</li>
                    <li>will</li>
                    <li>about</li>
                    <li>across</li>
                    <li>after</li>
                    <li>against</li>
                    <li>among</li>
                    <li>at</li>
                    <li>before</li>
                    <li>between</li>
                    <li>by</li>
                    <li>down</li>
                    <li>from</li>
                    <li>in</li>
                    <li>off</li>
                    <li>on</li>
                    <li>over</li>
                    <li>through</li>
                    <li>to</li>
                    <li>under</li>
                    <li>up</li>
                    <li>with</li>
                    <li>as</li>
                    <li>for</li>
                    <li>of</li>
                    <li>till</li>
                    <li>than</li>
                    <li>a</li>
                    <li>the</li>
                    <li>all</li>
                    <li>any</li>
                    <li>every</li>
                    <li>no</li>
                    <li>other</li>
                    <li>some</li>
                    <li>such</li>
                    <li>that</li>
                    <li>this</li>
                    <li>I</li>
                    <li>he</li>
                    <li>you</li>
                    <li>who</li>
                    <li>and</li>
                    <li>because</li>
                    <li>but</li>
                    <li>or</li>
                    <li>if</li>
                    <li>though</li>
                    <li>while</li>
                    <li>how</li>
                    <li>when</li>
                    <li>where</li>
                    <li>why</li>
                    <li>again</li>
                    <li>ever</li>
                    <li>far</li>
                    <li>forward</li>
                    <li>here</li>
                    <li>near</li>
                    <li>now</li>
                    <li>out</li>
                    <li>still</li>
                    <li>then</li>
                    <li>there</li>
                    <li>together</li>
                    <li>well</li>
                    <li>almost</li>
                    <li>enough</li>
                    <li>even</li>
                    <li>little</li>
                    <li>much</li>
                    <li>not</li>
                    <li>only</li>
                    <li>quite</li>
                    <li>so</li>
                    <li>very</li>
                    <li>tomorrow</li>
                    <li>yesterday</li>
                    <li>north</li>
                    <li>south</li>
                    <li>east</li>
                    <li>west</li>
                    <li>please</li>
                    <li>yes</li>
                </ul>
            </div>
        </div>
    </div>
</section>

<!-- Things — General -->
<section class="grade-section" id="things-general">
    <div class="grade-header">
        <div class="grade-num">2</div>
        <div>
            <div class="grade-title">Things — General</div>
            <div class="grade-sub">400 个普通名词 · 抽象概念与通用事物</div>
        </div>
    </div>
    <div class="semester-grid">
        <div class="semester-card s2">
            <div class="semester-header">
                <span class="semester-name">Things — General</span>
                <span class="difficulty-badge difficulty-high">400 words</span>
            </div>
            <div class="semester-body">
                <ul class="word-list">
                    <li>account</li>
                    <li>act</li>
                    <li>addition</li>
                    <li>adjustment</li>
                    <li>advertisement</li>
                    <li>agreement</li>
                    <li>air</li>
                    <li>amount</li>
                    <li>amusement</li>
                    <li>animal</li>
                    <li>answer</li>
                    <li>apparatus</li>
                    <li>approval</li>
                    <li>argument</li>
                    <li>art</li>
                    <li>attack</li>
                    <li>attempt</li>
                    <li>attention</li>
                    <li>attraction</li>
                    <li>authority</li>
                    <li>back</li>
                    <li>balance</li>
                    <li>base</li>
                    <li>behavior</li>
                    <li>belief</li>
                    <li>birth</li>
                    <li>bit</li>
                    <li>bite</li>
                    <li>blood</li>
                    <li>blow</li>
                    <li>body</li>
                    <li>brass</li>
                    <li>bread</li>
                    <li>breath</li>
                    <li>brother</li>
                    <li>building</li>
                    <li>burn</li>
                    <li>burst</li>
                    <li>business</li>
                    <li>butter</li>
                    <li>canvas</li>
                    <li>care</li>
                    <li>cause</li>
                    <li>chalk</li>
                    <li>chance</li>
                    <li>change</li>
                    <li>cloth</li>
                    <li>coal</li>
                    <li>color</li>
                    <li>comfort</li>
                    <li>committee</li>
                    <li>company</li>
                    <li>comparison</li>
                    <li>competition</li>
                    <li>condition</li>
                    <li>connection</li>
                    <li>control</li>
                    <li>cook</li>
                    <li>copper</li>
                    <li>copy</li>
                    <li>cork</li>
                    <li>cotton</li>
                    <li>cough</li>
                    <li>country</li>
                    <li>cover</li>
                    <li>crack</li>
                    <li>credit</li>
                    <li>crime</li>
                    <li>crush</li>
                    <li>cry</li>
                    <li>current</li>
                    <li>curve</li>
                    <li>damage</li>
                    <li>danger</li>
                    <li>daughter</li>
                    <li>day</li>
                    <li>death</li>
                    <li>debt</li>
                    <li>decision</li>
                    <li>degree</li>
                    <li>design</li>
                    <li>desire</li>
                    <li>destruction</li>
                    <li>detail</li>
                    <li>development</li>
                    <li>digestion</li>
                    <li>direction</li>
                    <li>discovery</li>
                    <li>discussion</li>
                    <li>disease</li>
                    <li>disgust</li>
                    <li>distance</li>
                    <li>distribution</li>
                    <li>division</li>
                    <li>doubt</li>
                    <li>drink</li>
                    <li>driving</li>
                    <li>dust</li>
                    <li>earth</li>
                    <li>edge</li>
                    <li>education</li>
                    <li>effect</li>
                    <li>end</li>
                    <li>error</li>
                    <li>event</li>
                    <li>example</li>
                    <li>exchange</li>
                    <li>existence</li>
                    <li>expansion</li>
                    <li>experience</li>
                    <li>expert</li>
                    <li>fact</li>
                    <li>fall</li>
                    <li>family</li>
                    <li>father</li>
                    <li>fear</li>
                    <li>feeling</li>
                    <li>fiction</li>
                    <li>field</li>
                    <li>fight</li>
                    <li>fire</li>
                    <li>flame</li>
                    <li>flight</li>
                    <li>flower</li>
                    <li>fold</li>
                    <li>food</li>
                    <li>force</li>
                    <li>form</li>
                    <li>friend</li>
                    <li>front</li>
                    <li>fruit</li>
                    <li>glass</li>
                    <li>gold</li>
                    <li>government</li>
                    <li>grain</li>
                    <li>grass</li>
                    <li>grip</li>
                    <li>group</li>
                    <li>growth</li>
                    <li>guide</li>
                    <li>harbor</li>
                    <li>harmony</li>
                    <li>hate</li>
                    <li>hearing</li>
                    <li>heat</li>
                    <li>help</li>
                    <li>history</li>
                    <li>hole</li>
                    <li>hope</li>
                    <li>hour</li>
                    <li>humor</li>
                    <li>ice</li>
                    <li>idea</li>
                    <li>impulse</li>
                    <li>increase</li>
                    <li>industry</li>
                    <li>ink</li>
                    <li>insect</li>
                    <li>instrument</li>
                    <li>insurance</li>
                    <li>interest</li>
                    <li>invention</li>
                    <li>iron</li>
                    <li>jelly</li>
                    <li>join</li>
                    <li>journey</li>
                    <li>judge</li>
                    <li>jump</li>
                    <li>kick</li>
                    <li>kiss</li>
                    <li>knowledge</li>
                    <li>land</li>
                    <li>language</li>
                    <li>laugh</li>
                    <li>law</li>
                    <li>lead</li>
                    <li>learning</li>
                    <li>leather</li>
                    <li>letter</li>
                    <li>level</li>
                    <li>lift</li>
                    <li>light</li>
                    <li>limit</li>
                    <li>linen</li>
                    <li>liquid</li>
                    <li>list</li>
                    <li>look</li>
                    <li>loss</li>
                    <li>love</li>
                    <li>machine</li>
                    <li>man</li>
                    <li>manager</li>
                    <li>mark</li>
                    <li>market</li>
                    <li>mass</li>
                    <li>meal</li>
                    <li>measure</li>
                    <li>meat</li>
                    <li>meeting</li>
                    <li>memory</li>
                    <li>metal</li>
                    <li>middle</li>
                    <li>milk</li>
                    <li>mind</li>
                    <li>mine</li>
                    <li>minute</li>
                    <li>mist</li>
                    <li>money</li>
                    <li>month</li>
                    <li>morning</li>
                    <li>mother</li>
                    <li>motion</li>
                    <li>mountain</li>
                    <li>move</li>
                    <li>music</li>
                    <li>name</li>
                    <li>nation</li>
                    <li>need</li>
                    <li>news</li>
                    <li>night</li>
                    <li>noise</li>
                    <li>note</li>
                    <li>number</li>
                    <li>observation</li>
                    <li>offer</li>
                    <li>oil</li>
                    <li>operation</li>
                    <li>opinion</li>
                    <li>order</li>
                    <li>organization</li>
                    <li>ornament</li>
                    <li>owner</li>
                    <li>page</li>
                    <li>pain</li>
                    <li>paint</li>
                    <li>paper</li>
                    <li>part</li>
                    <li>paste</li>
                    <li>payment</li>
                    <li>peace</li>
                    <li>person</li>
                    <li>place</li>
                    <li>plant</li>
                    <li>play</li>
                    <li>pleasure</li>
                    <li>point</li>
                    <li>poison</li>
                    <li>polish</li>
                    <li>porter</li>
                    <li>position</li>
                    <li>powder</li>
                    <li>power</li>
                    <li>price</li>
                    <li>process</li>
                    <li>produce</li>
                    <li>profit</li>
                    <li>property</li>
                    <li>prose</li>
                    <li>protest</li>
                    <li>pull</li>
                    <li>punishment</li>
                    <li>purpose</li>
                    <li>push</li>
                    <li>quality</li>
                    <li>question</li>
                    <li>rain</li>
                    <li>range</li>
                    <li>rate</li>
                    <li>ray</li>
                    <li>reaction</li>
                    <li>reading</li>
                    <li>reason</li>
                    <li>record</li>
                    <li>regret</li>
                    <li>relation</li>
                    <li>religion</li>
                    <li>representative</li>
                    <li>request</li>
                    <li>respect</li>
                    <li>rest</li>
                    <li>reward</li>
                    <li>rhythm</li>
                    <li>rice</li>
                    <li>river</li>
                    <li>road</li>
                    <li>roll</li>
                    <li>room</li>
                    <li>rub</li>
                    <li>rule</li>
                    <li>run</li>
                    <li>salt</li>
                    <li>sand</li>
                    <li>scale</li>
                    <li>science</li>
                    <li>sea</li>
                    <li>seat</li>
                    <li>secretary</li>
                    <li>selection</li>
                    <li>self</li>
                    <li>sense</li>
                    <li>servant</li>
                    <li>sex</li>
                    <li>shade</li>
                    <li>shake</li>
                    <li>shame</li>
                    <li>shock</li>
                    <li>side</li>
                    <li>sign</li>
                    <li>silk</li>
                    <li>silver</li>
                    <li>sister</li>
                    <li>size</li>
                    <li>sky</li>
                    <li>sleep</li>
                    <li>slip</li>
                    <li>slope</li>
                    <li>smash</li>
                    <li>smell</li>
                    <li>smile</li>
                    <li>smoke</li>
                    <li>sneeze</li>
                    <li>snow</li>
                    <li>soap</li>
                    <li>society</li>
                    <li>son</li>
                    <li>song</li>
                    <li>sort</li>
                    <li>sound</li>
                    <li>soup</li>
                    <li>space</li>
                    <li>stage</li>
                    <li>start</li>
                    <li>statement</li>
                    <li>steam</li>
                    <li>steel</li>
                    <li>step</li>
                    <li>stitch</li>
                    <li>stone</li>
                    <li>stop</li>
                    <li>story</li>
                    <li>stretch</li>
                    <li>structure</li>
                    <li>substance</li>
                    <li>sugar</li>
                    <li>suggestion</li>
                    <li>summer</li>
                    <li>support</li>
                    <li>surprise</li>
                    <li>swim</li>
                    <li>system</li>
                    <li>talk</li>
                    <li>taste</li>
                    <li>tax</li>
                    <li>teaching</li>
                    <li>tendency</li>
                    <li>test</li>
                    <li>theory</li>
                    <li>thing</li>
                    <li>thought</li>
                    <li>thunder</li>
                    <li>time</li>
                    <li>tin</li>
                    <li>top</li>
                    <li>touch</li>
                    <li>trade</li>
                    <li>transport</li>
                    <li>trick</li>
                    <li>trouble</li>
                    <li>turn</li>
                    <li>twist</li>
                    <li>unit</li>
                    <li>use</li>
                    <li>value</li>
                    <li>verse</li>
                    <li>vessel</li>
                    <li>view</li>
                    <li>voice</li>
                    <li>walk</li>
                    <li>war</li>
                    <li>wash</li>
                    <li>waste</li>
                    <li>water</li>
                    <li>wave</li>
                    <li>wax</li>
                    <li>way</li>
                    <li>weather</li>
                    <li>week</li>
                    <li>weight</li>
                    <li>wind</li>
                    <li>wine</li>
                    <li>winter</li>
                    <li>woman</li>
                    <li>wood</li>
                    <li>wool</li>
                    <li>word</li>
                    <li>work</li>
                    <li>wound</li>
                    <li>writing</li>
                    <li>year</li>
                </ul>
            </div>
        </div>
    </div>
</section>

<!-- Things — Picturable -->
<section class="grade-section" id="things-picturable">
    <div class="grade-header">
        <div class="grade-num">3</div>
        <div>
            <div class="grade-title">Things — Picturable</div>
            <div class="grade-sub">200 个具象名词 · 可视觉化的事物</div>
        </div>
    </div>
    <div class="semester-grid">
        <div class="semester-card s3">
            <div class="semester-header">
                <span class="semester-name">Things — Picturable</span>
                <span class="difficulty-badge difficulty-medium">200 words</span>
            </div>
            <div class="semester-body">
                <ul class="word-list">
                    <li>angle</li>
                    <li>ant</li>
                    <li>apple</li>
                    <li>arch</li>
                    <li>arm</li>
                    <li>army</li>
                    <li>baby</li>
                    <li>bag</li>
                    <li>ball</li>
                    <li>band</li>
                    <li>basin</li>
                    <li>basket</li>
                    <li>bath</li>
                    <li>bed</li>
                    <li>bee</li>
                    <li>bell</li>
                    <li>berry</li>
                    <li>bird</li>
                    <li>blade</li>
                    <li>board</li>
                    <li>boat</li>
                    <li>bone</li>
                    <li>book</li>
                    <li>boot</li>
                    <li>bottle</li>
                    <li>box</li>
                    <li>boy</li>
                    <li>brain</li>
                    <li>brake</li>
                    <li>branch</li>
                    <li>brick</li>
                    <li>bridge</li>
                    <li>brush</li>
                    <li>bucket</li>
                    <li>bulb</li>
                    <li>button</li>
                    <li>cake</li>
                    <li>camera</li>
                    <li>card</li>
                    <li>cart</li>
                    <li>carriage</li>
                    <li>cat</li>
                    <li>chain</li>
                    <li>cheese</li>
                    <li>chest</li>
                    <li>chin</li>
                    <li>church</li>
                    <li>circle</li>
                    <li>clock</li>
                    <li>cloud</li>
                    <li>coat</li>
                    <li>collar</li>
                    <li>comb</li>
                    <li>cord</li>
                    <li>cow</li>
                    <li>cup</li>
                    <li>curtain</li>
                    <li>cushion</li>
                    <li>dog</li>
                    <li>door</li>
                    <li>drain</li>
                    <li>drawer</li>
                    <li>dress</li>
                    <li>drop</li>
                    <li>ear</li>
                    <li>egg</li>
                    <li>engine</li>
                    <li>eye</li>
                    <li>face</li>
                    <li>farm</li>
                    <li>feather</li>
                    <li>finger</li>
                    <li>fish</li>
                    <li>flag</li>
                    <li>floor</li>
                    <li>fly</li>
                    <li>foot</li>
                    <li>fork</li>
                    <li>fowl</li>
                    <li>frame</li>
                    <li>garden</li>
                    <li>girl</li>
                    <li>glove</li>
                    <li>goat</li>
                    <li>gun</li>
                    <li>hair</li>
                    <li>hammer</li>
                    <li>hand</li>
                    <li>hat</li>
                    <li>head</li>
                    <li>heart</li>
                    <li>hook</li>
                    <li>horn</li>
                    <li>horse</li>
                    <li>hospital</li>
                    <li>house</li>
                    <li>island</li>
                    <li>jewel</li>
                    <li>kettle</li>
                    <li>key</li>
                    <li>knee</li>
                    <li>knife</li>
                    <li>knot</li>
                    <li>leaf</li>
                    <li>leg</li>
                    <li>library</li>
                    <li>line</li>
                    <li>lip</li>
                    <li>lock</li>
                    <li>map</li>
                    <li>match</li>
                    <li>monkey</li>
                    <li>moon</li>
                    <li>mouth</li>
                    <li>muscle</li>
                    <li>nail</li>
                    <li>neck</li>
                    <li>needle</li>
                    <li>nerve</li>
                    <li>net</li>
                    <li>nose</li>
                    <li>nut</li>
                    <li>office</li>
                    <li>orange</li>
                    <li>oven</li>
                    <li>parcel</li>
                    <li>pen</li>
                    <li>pencil</li>
                    <li>picture</li>
                    <li>pig</li>
                    <li>pin</li>
                    <li>pipe</li>
                    <li>plane</li>
                    <li>plate</li>
                    <li>plough</li>
                    <li>pocket</li>
                    <li>pot</li>
                    <li>potato</li>
                    <li>prison</li>
                    <li>pump</li>
                    <li>rail</li>
                    <li>rat</li>
                    <li>receipt</li>
                    <li>ring</li>
                    <li>rod</li>
                    <li>roof</li>
                    <li>root</li>
                    <li>sail</li>
                    <li>school</li>
                    <li>scissors</li>
                    <li>screw</li>
                    <li>seed</li>
                    <li>sheep</li>
                    <li>shelf</li>
                    <li>ship</li>
                    <li>shirt</li>
                    <li>shoe</li>
                    <li>skin</li>
                    <li>skirt</li>
                    <li>snake</li>
                    <li>sock</li>
                    <li>spade</li>
                    <li>sponge</li>
                    <li>spoon</li>
                    <li>spring</li>
                    <li>square</li>
                    <li>stamp</li>
                    <li>star</li>
                    <li>station</li>
                    <li>stem</li>
                    <li>stick</li>
                    <li>store</li>
                    <li>street</li>
                    <li>string</li>
                    <li>sun</li>
                    <li>table</li>
                    <li>tail</li>
                    <li>thread</li>
                    <li>throat</li>
                    <li>thumb</li>
                    <li>ticket</li>
                    <li>toe</li>
                    <li>tongue</li>
                    <li>tooth</li>
                    <li>town</li>
                    <li>train</li>
                    <li>tray</li>
                    <li>tree</li>
                    <li>trousers</li>
                    <li>umbrella</li>
                    <li>wall</li>
                    <li>watch</li>
                    <li>wheel</li>
                    <li>whip</li>
                    <li>whistle</li>
                    <li>window</li>
                    <li>wing</li>
                    <li>wire</li>
                    <li>worm</li>
                </ul>
            </div>
        </div>
    </div>
</section>

<!-- Qualities -->
<section class="grade-section" id="qualities">
    <div class="grade-header">
        <div class="grade-num">4</div>
        <div>
            <div class="grade-title">Qualities</div>
            <div class="grade-sub">150 个形容词 · 描述性质与状态</div>
        </div>
    </div>
    <div class="semester-grid">
        <div class="semester-card s4">
            <div class="semester-header">
                <span class="semester-name">Qualities</span>
                <span class="difficulty-badge difficulty-medium">150 words</span>
            </div>
            <div class="semester-body">
                <ul class="word-list">
                    <li>able</li>
                    <li>acid</li>
                    <li>angry</li>
                    <li>automatic</li>
                    <li>beautiful</li>
                    <li>black</li>
                    <li>boiling</li>
                    <li>bright</li>
                    <li>broken</li>
                    <li>brown</li>
                    <li>cheap</li>
                    <li>chemical</li>
                    <li>chief</li>
                    <li>clean</li>
                    <li>clear</li>
                    <li>cold</li>
                    <li>common</li>
                    <li>complete</li>
                    <li>complex</li>
                    <li>conscious</li>
                    <li>cruel</li>
                    <li>cut</li>
                    <li>deep</li>
                    <li>dependent</li>
                    <li>early</li>
                    <li>elastic</li>
                    <li>electric</li>
                    <li>equal</li>
                    <li>fat</li>
                    <li>fertile</li>
                    <li>first</li>
                    <li>fixed</li>
                    <li>flat</li>
                    <li>free</li>
                    <li>frequent</li>
                    <li>full</li>
                    <li>general</li>
                    <li>good</li>
                    <li>great</li>
                    <li>grey</li>
                    <li>hanging</li>
                    <li>happy</li>
                    <li>hard</li>
                    <li>healthy</li>
                    <li>high</li>
                    <li>hollow</li>
                    <li>important</li>
                    <li>kind</li>
                    <li>like</li>
                    <li>living</li>
                    <li>long</li>
                    <li>male</li>
                    <li>married</li>
                    <li>material</li>
                    <li>medical</li>
                    <li>military</li>
                    <li>mixed</li>
                    <li>natural</li>
                    <li>necessary</li>
                    <li>new</li>
                    <li>normal</li>
                    <li>open</li>
                    <li>parallel</li>
                    <li>past</li>
                    <li>physical</li>
                    <li>political</li>
                    <li>poor</li>
                    <li>possible</li>
                    <li>present</li>
                    <li>private</li>
                    <li>probable</li>
                    <li>public</li>
                    <li>quick</li>
                    <li>quiet</li>
                    <li>ready</li>
                    <li>red</li>
                    <li>regular</li>
                    <li>responsible</li>
                    <li>right</li>
                    <li>round</li>
                    <li>same</li>
                    <li>second</li>
                    <li>separate</li>
                    <li>serious</li>
                    <li>sharp</li>
                    <li>smooth</li>
                    <li>sticky</li>
                    <li>stiff</li>
                    <li>straight</li>
                    <li>strong</li>
                    <li>sudden</li>
                    <li>sweet</li>
                    <li>tall</li>
                    <li>thick</li>
                    <li>tight</li>
                    <li>tired</li>
                    <li>true</li>
                    <li>violent</li>
                    <li>waiting</li>
                    <li>warm</li>
                    <li>wet</li>
                    <li>wide</li>
                    <li>wise</li>
                    <li>yellow</li>
                    <li>young</li>
                    <li>awake</li>
                    <li>bad</li>
                    <li>bent</li>
                    <li>bitter</li>
                    <li>blue</li>
                    <li>certain</li>
                    <li>comfortable</li>
                    <li>cruel</li>
                    <li>dark</li>
                    <li>dead</li>
                    <li>dear</li>
                    <li>delicate</li>
                    <li>different</li>
                    <li>dirty</li>
                    <li>dry</li>
                    <li>false</li>
                    <li>feeble</li>
                    <li>female</li>
                    <li>foolish</li>
                    <li>future</li>
                    <li>green</li>
                    <li>ill</li>
                    <li>last</li>
                    <li>late</li>
                    <li>left</li>
                    <li>loose</li>
                    <li>loud</li>
                    <li>low</li>
                    <li>mixed</li>
                    <li>narrow</li>
                    <li>old</li>
                    <li>opposite</li>
                    <li>public</li>
                    <li>rough</li>
                    <li>sad</li>
                    <li>safe</li>
                    <li>secret</li>
                    <li>short</li>
                    <li>shut</li>
                    <li>simple</li>
                    <li>slow</li>
                    <li>small</li>
                    <li>soft</li>
                    <li>solid</li>
                    <li>special</li>
                    <li>strange</li>
                    <li>thin</li>
                    <li>white</li>
                    <li>wrong</li>
                </ul>
            </div>
        </div>
    </div>
</section>

<!-- Examples of Word Order -->
<section class="grade-section" id="wordorder">
    <div class="grade-header">
        <div class="grade-num">5</div>
        <div>
            <div class="grade-title">Examples of Word Order</div>
            <div class="grade-sub">词序示例 · 展示 850 词如何组合成句</div>
        </div>
    </div>
    <div class="semester-grid">
        <div class="semester-card s5">
            <div class="semester-header">
                <span class="semester-name">Examples</span>
                <span class="difficulty-badge difficulty-medium">22 phrases</span>
            </div>
            <div class="semester-body">
                <div class="examples">
                    <div class="example-item">the camera</div>
                    <div class="example-item">man who</div>
                    <div class="example-item">made an</div>
                    <div class="example-item">attempt to</div>
                    <div class="example-item">take a</div>
                    <div class="example-item">moving picture</div>
                    <div class="example-item">of the society</div>
                    <div class="example-item">women before</div>
                    <div class="example-item">they got their</div>
                    <div class="example-item">hats off</div>
                    <div class="example-item">did not get off</div>
                    <div class="example-item">the ship till</div>
                    <div class="example-item">he was questioned</div>
                    <div class="example-item">by the police</div>
                    <div class="example-item">we will give</div>
                    <div class="example-item">simple rules</div>
                    <div class="example-item">covering the</div>
                    <div class="example-item">formation of</div>
                    <div class="example-item">plurals compounds</div>
                    <div class="example-item">derivatives</div>
                    <div class="example-item">comparatives and</div>
                    <div class="example-item">adverbs</div>
                </div>
            </div>
        </div>
    </div>
</section>

<!-- 附录说明 -->
<section class="appendix">
    <div class="appendix-box">
        <strong>说明：</strong><br>
        1. <strong>Basic English</strong> 由 C.K. Ogden 于 1930 年设计，850 个核心词汇覆盖牛津袖珍英语词典 90% 的概念。<br>
        2. 词汇分为 5 大类：Operations（100）、Things — General（400）、Things — Picturable（200）、Qualities（150）、Examples（22）。<br>
        3. 本页面支持响应式浏览，在手机和电脑上均有良好体验。
    </div>
</section>

<!-- 打印版入口 -->
<section class="grade-section" style="padding-top:0;">
    <div class="semester-card s5">
        <div class="semester-header">
            <span class="semester-name">打印版入口</span>
            <span class="difficulty-badge difficulty-medium">A4 排版</span>
        </div>
        <div class="semester-body">
            <p style="font-size:14px;color:var(--text-light);margin-bottom:12px;">需要打印或保存 PDF？点击下方按钮，在新标签页打开 A4 排版版本。</p>
            <a href="basic_english_850_print.html" target="_blank" class="share-btn primary" style="display:inline-flex;">打开打印版（新页面）</a>
        </div>
    </div>
</section>

<!-- 底部分享 -->
<div class="share-bar">
    <a href="basic_english_850_print.html" target="_blank" class="share-btn secondary">打印/保存PDF</a>
    <button class="share-btn primary" onclick="copyLink()">复制链接分享</button>
</div>

<!-- 单词信息卡片 -->
<div id="wordInfo" class="word-info">
    <div class="word-info-word" id="infoWord"></div>
    <div class="word-info-phonetic" id="infoPhonetic"></div>
    <div class="word-info-meaning" id="infoMeaning"></div>
</div>

<script>
    // 单词数据（包含音标和中文翻译）
    const wordData = {
        'come': { phonetic: '/kʌm/', meaning: '来；到达；变得' },
        'get': { phonetic: '/ɡet/', meaning: '得到；获得；到达；变得' },
        'give': { phonetic: '/ɡɪv/', meaning: '给；给予；提供' },
        'go': { phonetic: '/ɡəʊ/', meaning: '去；走；进行；离开' },
        'keep': { phonetic: '/kiːp/', meaning: '保持；保存；遵守' },
        'let': { phonetic: '/let/', meaning: '让；允许；出租' },
        'make': { phonetic: '/meɪk/', meaning: '制作；使得；进行' },
        'put': { phonetic: '/pʊt/', meaning: '放；放置；放置' },
        'seem': { phonetic: '/siːm/', meaning: '似乎；好像；看起来' },
        'take': { phonetic: '/teɪk/', meaning: '拿；取；带走；花费' },
        'be': { phonetic: '/biː/', meaning: '是；存在；成为' },
        'do': { phonetic: '/duː/', meaning: '做；干；进行' },
        'have': { phonetic: '/hæv/', meaning: '有；拥有；进行' },
        'say': { phonetic: '/seɪ/', meaning: '说；讲；表明' },
        'see': { phonetic: '/siː/', meaning: '看见；理解；明白' },
        'send': { phonetic: '/send/', meaning: '发送；寄；派遣' },
        'may': { phonetic: '/meɪ/', meaning: '可能；也许；可以' },
        'will': { phonetic: '/wɪl/', meaning: '将要；会；愿意' },
        'about': { phonetic: '/əˈbaʊt/', meaning: '关于；大约；在周围' },
        'across': { phonetic: '/əˈkrɒs/', meaning: '穿过；横穿；在对面' },
        'after': { phonetic: '/ˈɑːftə(r)/', meaning: '在…之后；在…后面' },
        'against': { phonetic: '/əˈɡenst/', meaning: '反对；违反；紧靠' },
        'among': { phonetic: '/əˈmʌŋ/', meaning: '在…之中；在…之间' },
        'at': { phonetic: '/æt/', meaning: '在（表示存在或出现的地点、场所、位置、空间）' },
        'before': { phonetic: '/bɪˈfɔː(r)/', meaning: '在…之前；在…前面' },
        'between': { phonetic: '/bɪˈtwiːn/', meaning: '在…之间；在…中间' },
        'by': { phonetic: '/baɪ/', meaning: '在…旁边；通过；被' },
        'down': { phonetic: '/daʊn/', meaning: '向下；在下面' },
        'from': { phonetic: '/frɒm/', meaning: '从…；来自…' },
        'in': { phonetic: '/ɪn/', meaning: '在…里面；在…之内' },
        'off': { phonetic: '/ɒf/', meaning: '离开；脱落' },
        'on': { phonetic: '/ɒn/', meaning: '在…上面；关于' },
        'over': { phonetic: '/ˈəʊvə(r)/', meaning: '在…之上；越过；超过' },
        'through': { phonetic: '/θruː/', meaning: '穿过；通过；从始至终' },
        'to': { phonetic: '/tuː/', meaning: '到；向；往' },
        'under': { phonetic: '/ˈʌndə(r)/', meaning: '在…下面；在…之下' },
        'up': { phonetic: '/ʌp/', meaning: '向上；在上面' },
        'with': { phonetic: '/wɪð/', meaning: '和…一起；具有；用' },
        'as': { phonetic: '/æz/', meaning: '作为；像…一样；当…时' },
        'for': { phonetic: '/fɔː(r)/', meaning: '为了；对于；因为' },
        'of': { phonetic: '/ɒv/', meaning: '…的；关于' },
        'till': { phonetic: '/tɪl/', meaning: '直到…为止' },
        'than': { phonetic: '/ðæn/', meaning: '比（用于比较级）' },
        'a': { phonetic: '/ə/', meaning: '一个（不定冠词）' },
        'the': { phonetic: '/ðə/', meaning: '这；那（定冠词）' },
        'all': { phonetic: '/ɔːl/', meaning: '全部；所有' },
        'any': { phonetic: '/ˈeni/', meaning: '任何；一些' },
        'every': { phonetic: '/ˈevri/', meaning: '每个；每一' },
        'no': { phonetic: '/nəʊ/', meaning: '不；没有' },
        'other': { phonetic: '/ˈʌðə(r)/', meaning: '其他的；另外的' },
        'some': { phonetic: '/sʌm/', meaning: '一些；有些；某个' },
        'such': { phonetic: '/sʌtʃ/', meaning: '这样的；如此的' },
        'that': { phonetic: '/ðæt/', meaning: '那；那个' },
        'this': { phonetic: '/ðɪs/', meaning: '这；这个' },
        'I': { phonetic: '/aɪ/', meaning: '我' },
        'he': { phonetic: '/hiː/', meaning: '他' },
        'you': { phonetic: '/juː/', meaning: '你；你们' },
        'who': { phonetic: '/huː/', meaning: '谁；什么人' },
        'and': { phonetic: '/ænd/', meaning: '和；与；并且' },
        'because': { phonetic: '/bɪˈkɒz/', meaning: '因为' },
        'but': { phonetic: '/bʌt/', meaning: '但是；然而' },
        'or': { phonetic: '/ɔː(r)/', meaning: '或者；还是' },
        'if': { phonetic: '/ɪf/', meaning: '如果；假如' },
        'though': { phonetic: '/ðəʊ/', meaning: '虽然；尽管' },
        'while': { phonetic: '/waɪl/', meaning: '当…的时候；然而' },
        'how': { phonetic: '/haʊ/', meaning: '怎样；如何' },
        'when': { phonetic: '/wen/', meaning: '什么时候；当…时' },
        'where': { phonetic: '/weə(r)/', meaning: '哪里；在…地方' },
        'why': { phonetic: '/waɪ/', meaning: '为什么' },
        'again': { phonetic: '/əˈɡen/', meaning: '再一次；又' },
        'ever': { phonetic: '/ˈevə(r)/', meaning: '曾经；永远' },
        'far': { phonetic: '/fɑː(r)/', meaning: '远的；遥远的' },
        'forward': { phonetic: '/ˈfɔːwəd/', meaning: '向前；前进' },
        'here': { phonetic: '/hɪə(r)/', meaning: '在这里；这里' },
        'near': { phonetic: '/nɪə(r)/', meaning: '近的；接近' },
        'now': { phonetic: '/naʊ/', meaning: '现在；此刻' },
        'out': { phonetic: '/aʊt/', meaning: '出来；向外' },
        'still': { phonetic: '/stɪl/', meaning: '仍然；还；静止的' },
        'then': { phonetic: '/ðen/', meaning: '然后；那时；那么' },
        'there': { phonetic: '/ðeə(r)/', meaning: '那里；在那里' },
        'together': { phonetic: '/təˈɡeðə(r)/', meaning: '一起；共同' },
        'well': { phonetic: '/wel/', meaning: '好；令人满意地；健康的' },
        'almost': { phonetic: '/ˈɔːlməʊst/', meaning: '几乎；差不多' },
        'enough': { phonetic: '/ɪˈnʌf/', meaning: '足够的；充足的' },
        'even': { phonetic: '/ˈiːvn/', meaning: '甚至；连；即使' },
        'little': { phonetic: '/ˈlɪtl/', meaning: '小的；很少的' },
        'much': { phonetic: '/mʌtʃ/', meaning: '很多的；大量的' },
        'not': { phonetic: '/nɒt/', meaning: '不；没有' },
        'only': { phonetic: '/ˈəʊnli/', meaning: '只有；仅仅' },
        'quite': { phonetic: '/kwaɪt/', meaning: '相当；十分；完全' },
        'so': { phonetic: '/səʊ/', meaning: '如此；所以；因此' },
        'very': { phonetic: '/ˈveri/', meaning: '非常；很' },
        'tomorrow': { phonetic: '/təˈmɒrəʊ/', meaning: '明天；明日' },
        'yesterday': { phonetic: '/ˈjestədeɪ/', meaning: '昨天；昨日' },
        'north': { phonetic: '/nɔːθ/', meaning: '北方；北部' },
        'south': { phonetic: '/saʊθ/', meaning: '南方；南部' },
        'east': { phonetic: '/iːst/', meaning: '东方；东部' },
        'west': { phonetic: '/west/', meaning: '西方；西部' },
        'please': { phonetic: '/pliːz/', meaning: '请；使高兴' },
        'yes': { phonetic: '/jes/', meaning: '是；是的' },
        // Things — General
        'account': { phonetic: '/əˈkaʊnt/', meaning: '账户；描述；说明' },
        'act': { phonetic: '/ækt/', meaning: '行动；表现；起作用' },
        'addition': { phonetic: '/əˈdɪʃn/', meaning: '加法；增加；添加物' },
        'adjustment': { phonetic: '/əˈdʒʌstmənt/', meaning: '调整；调节' },
        'advertisement': { phonetic: '/ədˈvɜːtɪsmənt/', meaning: '广告；宣传' },
        'agreement': { phonetic: '/əˈɡriːmənt/', meaning: '协议；同意；一致' },
        'air': { phonetic: '/eə(r)/', meaning: '空气；大气' },
        'amount': { phonetic: '/əˈmaʊnt/', meaning: '数量；数额' },
        'amusement': { phonetic: '/əˈmjuːzmənt/', meaning: '娱乐；消遣；乐趣' },
        'animal': { phonetic: '/ˈænɪml/', meaning: '动物' },
        'answer': { phonetic: '/ˈɑːnsə(r)/', meaning: '回答；答案' },
        'apparatus': { phonetic: '/ˌæpəˈreɪtəs/', meaning: '装置；设备；仪器' },
        'approval': { phonetic: '/əˈpruːvl/', meaning: '批准；认可；赞成' },
        'argument': { phonetic: '/ˈɑːɡjumənt/', meaning: '争论；论点；论证' },
        'art': { phonetic: '/ɑːt/', meaning: '艺术；美术；技艺' },
        'attack': { phonetic: '/əˈtæk/', meaning: '攻击；袭击；发作' },
        'attempt': { phonetic: '/əˈtempt/', meaning: '尝试；企图；试图' },
        'attention': { phonetic: '/əˈtenʃn/', meaning: '注意；注意力；留心' },
        'attraction': { phonetic: '/əˈtrækʃn/', meaning: '吸引；吸引力；引力' },
        'authority': { phonetic: '/ɔːˈθɒrəti/', meaning: '权威；当局；权力' },
        'back': { phonetic: '/bæk/', meaning: '背部；后面；返回' },
        'balance': { phonetic: '/ˈbæləns/', meaning: '平衡；均衡；天平' },
        'base': { phonetic: '/beɪs/', meaning: '基础；基地；底部' },
        'behavior': { phonetic: '/bɪˈheɪvjə(r)/', meaning: '行为；举止；表现' },
        'belief': { phonetic: '/bɪˈliːf/', meaning: '相信；信念；信仰' },
        'birth': { phonetic: '/bɜːθ/', meaning: '出生；诞生；分娩' },
        'bit': { phonetic: '/bɪt/', meaning: '一点；少量；比特' },
        'bite': { phonetic: '/baɪt/', meaning: '咬；叮；刺痛' },
        'blood': { phonetic: '/blʌd/', meaning: '血；血液' },
        'blow': { phonetic: '/bləʊ/', meaning: '吹；刮；打击' },
        'body': { phonetic: '/ˈbɒdi/', meaning: '身体；主体；尸体' },
        'brass': { phonetic: '/brɑːs/', meaning: '黄铜；铜管乐器' },
        'bread': { phonetic: '/bred/', meaning: '面包；生计' },
        'breath': { phonetic: '/breθ/', meaning: '呼吸；气息' },
        'brother': { phonetic: '/ˈbrʌðə(r)/', meaning: '兄弟；同胞' },
        'building': { phonetic: '/ˈbɪldɪŋ/', meaning: '建筑物；楼房' },
        'burn': { phonetic: '/bɜːn/', meaning: '燃烧；灼伤；烧伤' },
        'burst': { phonetic: '/bɜːst/', meaning: '爆发；爆裂；突发' },
        'business': { phonetic: '/ˈbɪznəs/', meaning: '商业；生意；事务' },
        'butter': { phonetic: '/ˈbʌtə(r)/', meaning: '黄油；奶油' },
        'canvas': { phonetic: '/ˈkænvəs/', meaning: '帆布；画布' },
        'care': { phonetic: '/keə(r)/', meaning: '关心；照顾；小心' },
        'cause': { phonetic: '/kɔːz/', meaning: '原因；导致；引起' },
        'chalk': { phonetic: '/tʃɔːk/', meaning: '粉笔；白垩' },
        'chance': { phonetic: '/tʃɑːns/', meaning: '机会；可能性；运气' },
        'change': { phonetic: '/tʃeɪndʒ/', meaning: '改变；变化；零钱' },
        'cloth': { phonetic: '/klɒθ/', meaning: '布；织物；布料' },
        'coal': { phonetic: '/kəʊl/', meaning: '煤；煤炭' },
        'color': { phonetic: '/ˈkʌlə(r)/', meaning: '颜色；色彩' },
        'comfort': { phonetic: '/ˈkʌmfət/', meaning: '舒适；安慰；慰藉' },
        'committee': { phonetic: '/kəˈmɪti/', meaning: '委员会' },
        'company': { phonetic: '/ˈkʌmpəni/', meaning: '公司；陪伴；同伴' },
        'comparison': { phonetic: '/kəmˈpærɪsn/', meaning: '比较；对比；比喻' },
        'competition': { phonetic: '/ˌkɒmpəˈtɪʃn/', meaning: '竞争；比赛；竞赛' },
        'condition': { phonetic: '/kənˈdɪʃn/', meaning: '条件；状况；环境' },
        'connection': { phonetic: '/kəˈnekʃn/', meaning: '连接；联系；关系' },
        'control': { phonetic: '/kənˈtrəʊl/', meaning: '控制；支配；管理' },
        'cook': { phonetic: '/kʊk/', meaning: '烹调；煮；厨师' },
        'copper': { phonetic: '/ˈkɒpə(r)/', meaning: '铜；铜币' },
        'copy': { phonetic: '/ˈkɒpi/', meaning: '复制；副本；拷贝' },
        'cork': { phonetic: '/kɔːk/', meaning: '软木；软木塞' },
        'cotton': { phonetic: '/ˈkɒtn/', meaning: '棉花；棉布' },
        'cough': { phonetic: '/kɒf/', meaning: '咳嗽；咳嗽声' },
        'country': { phonetic: '/ˈkʌntri/', meaning: '国家；乡村；乡下' },
        'cover': { phonetic: '/ˈkʌvə(r)/', meaning: '覆盖；遮盖；封面' },
        'crack': { phonetic: '/kræk/', meaning: '裂缝；裂纹；破裂' },
        'credit': { phonetic: '/ˈkredɪt/', meaning: '信用；信贷；荣誉' },
        'crime': { phonetic: '/kraɪm/', meaning: '罪行；犯罪；罪恶' },
        'crush': { phonetic: '/krʌʃ/', meaning: '压碎；粉碎；迷恋' },
        'cry': { phonetic: '/kraɪ/', meaning: '哭；叫喊；哭泣' },
        'current': { phonetic: '/ˈkʌrənt/', meaning: '现在的；当前的；电流' },
        'curve': { phonetic: '/kɜːv/', meaning: '曲线；弯曲；弧线' },
        'damage': { phonetic: '/ˈdæmɪdʒ/', meaning: '损害；损坏；损失' },
        'danger': { phonetic: '/ˈdeɪndʒə(r)/', meaning: '危险；风险；威胁' },
        'daughter': { phonetic: '/ˈdɔːtə(r)/', meaning: '女儿' },
        'day': { phonetic: '/deɪ/', meaning: '一天；白天；日子' },
        'death': { phonetic: '/deθ/', meaning: '死亡；逝世；死神' },
        'debt': { phonetic: '/det/', meaning: '债务；欠款' },
        'decision': { phonetic: '/dɪˈsɪʒn/', meaning: '决定；决心；决策' },
        'degree': { phonetic: '/dɪˈɡriː/', meaning: '程度；度数；学位' },
        'design': { phonetic: '/dɪˈzaɪn/', meaning: '设计；图案；构思' },
        'desire': { phonetic: '/dɪˈzaɪə(r)/', meaning: '渴望；欲望；愿望' },
        'destruction': { phonetic: '/dɪˈstrʌkʃn/', meaning: '破坏；毁灭；摧毁' },
        'detail': { phonetic: '/ˈdiːteɪl/', meaning: '细节；详情；详细' },
        'development': { phonetic: '/dɪˈveləpmənt/', meaning: '发展；开发；生长' },
        'digestion': { phonetic: '/daɪˈdʒestʃən/', meaning: '消化；领悟' },
        'direction': { phonetic: '/daɪˈrekʃn/', meaning: '方向；指导；趋势' },
        'discovery': { phonetic: '/dɪˈskʌvəri/', meaning: '发现；发觉；被发现的事物' },
        'discussion': { phonetic: '/dɪˈskʌʃn/', meaning: '讨论；商讨；论述' },
        'disease': { phonetic: '/dɪˈziːz/', meaning: '疾病；弊病' },
        'disgust': { phonetic: '/dɪsˈɡʌst/', meaning: '厌恶；憎恶；反感' },
        'distance': { phonetic: '/ˈdɪstəns/', meaning: '距离；远方；疏远' },
        'distribution': { phonetic: '/ˌdɪstrɪˈbjuːʃn/', meaning: '分配；分发；分布' },
        'division': { phonetic: '/dɪˈvɪʒn/', meaning: '分割；除法；部门' },
        'doubt': { phonetic: '/daʊt/', meaning: '怀疑；疑问；疑虑' },
        'drink': { phonetic: '/drɪŋk/', meaning: '喝；饮；饮料' },
        'driving': { phonetic: '/ˈdraɪvɪŋ/', meaning: '驾驶；驱动；推进' },
        'dust': { phonetic: '/dʌst/', meaning: '灰尘；尘土；尘埃' },
        'earth': { phonetic: '/ɜːθ/', meaning: '地球；泥土；大地' },
        'edge': { phonetic: '/edʒ/', meaning: '边缘；边；刃' },
        'education': { phonetic: '/ˌedʒuˈkeɪʃn/', meaning: '教育；培养；训练' },
        'effect': { phonetic: '/ɪˈfekt/', meaning: '效果；影响；作用' },
        'end': { phonetic: '/end/', meaning: '结束；末端；尽头' },
        'error': { phonetic: '/ˈerə(r)/', meaning: '错误；差错；谬误' },
        'event': { phonetic: '/ɪˈvent/', meaning: '事件；大事；比赛项目' },
        'example': { phonetic: '/ɪɡˈzɑːmpl/', meaning: '例子；榜样；范例' },
        'exchange': { phonetic: '/ɪksˈtʃeɪndʒ/', meaning: '交换；交流；兑换' },
        'existence': { phonetic: '/ɪɡˈzɪstəns/', meaning: '存在；生存；生活' },
        'expansion': { phonetic: '/ɪkˈspænʃn/', meaning: '扩大；扩展；膨胀' },
        'experience': { phonetic: '/ɪkˈspɪəriəns/', meaning: '经验；经历；体验' },
        'expert': { phonetic: '/ˈekspɜːt/', meaning: '专家；能手；行家' },
        'fact': { phonetic: '/fækt/', meaning: '事实；真相；实际' },
        'fall': { phonetic: '/fɔːl/', meaning: '落下；跌倒；下降' },
        'family': { phonetic: '/ˈfæməli/', meaning: '家庭；家族；亲属' },
        'father': { phonetic: '/ˈfɑːðə(r)/', meaning: '父亲；爸爸；奠基者' },
        'fear': { phonetic: '/fɪə(r)/', meaning: '害怕；恐惧；担心' },
        'feeling': { phonetic: '/ˈfiːlɪŋ/', meaning: '感觉；感情；情绪' },
        'fiction': { phonetic: '/ˈfɪkʃn/', meaning: '小说；虚构；杜撰' },
        'field': { phonetic: '/fiːld/', meaning: '田野；领域；场地' },
        'fight': { phonetic: '/faɪt/', meaning: '打架；战斗；斗争' },
        'fire': { phonetic: '/ˈfaɪə(r)/', meaning: '火；火灾；开火' },
        'flame': { phonetic: '/fleɪm/', meaning: '火焰；激情；火舌' },
        'flight': { phonetic: '/flaɪt/', meaning: '飞行；航班；逃跑' },
        'flower': { phonetic: '/ˈflaʊə(r)/', meaning: '花；花卉；精华' },
        'fold': { phonetic: '/fəʊld/', meaning: '折叠；折痕；羊栏' },
        'food': { phonetic: '/fuːd/', meaning: '食物；食品；养料' },
        'force': { phonetic: '/fɔːs/', meaning: '力量；武力；强迫' },
        'form': { phonetic: '/fɔːm/', meaning: '形式；形状；表格' },
        'friend': { phonetic: '/frend/', meaning: '朋友；友人；赞助者' },
        'front': { phonetic: '/frʌnt/', meaning: '前面；正面；前线' },
        'fruit': { phonetic: '/fruːt/', meaning: '水果；果实；成果' },
        'glass': { phonetic: '/ɡlɑːs/', meaning: '玻璃；玻璃杯；镜子' },
        'gold': { phonetic: '/ɡəʊld/', meaning: '金；黄金；金色' },
        'government': { phonetic: '/ˈɡʌvənmənt/', meaning: '政府；内阁；治理' },
        'grain': { phonetic: '/ɡreɪn/', meaning: '谷物；颗粒；纹理' },
        'grass': { phonetic: '/ɡrɑːs/', meaning: '草；草地；草坪' },
        'grip': { phonetic: '/ɡrɪp/', meaning: '紧握；抓牢；掌握' },
        'group': { phonetic: '/ɡruːp/', meaning: '组；群；团体' },
        'growth': { phonetic: '/ɡrəʊθ/', meaning: '生长；增长；发展' },
        'guide': { phonetic: '/ɡaɪd/', meaning: '引导；向导；指南' },
        'harbor': { phonetic: '/ˈhɑːbə(r)/', meaning: '港口；海港；避难所' },
        'harmony': { phonetic: '/ˈhɑːməni/', meaning: '和谐；协调；融洽' },
        'hate': { phonetic: '/heɪt/', meaning: '憎恨；厌恶；仇恨' },
        'hearing': { phonetic: '/ˈhɪərɪŋ/', meaning: '听觉；听力；审讯' },
        'heat': { phonetic: '/hiːt/', meaning: '热；热量；高温' },
        'help': { phonetic: '/help/', meaning: '帮助；协助；援助' },
        'history': { phonetic: '/ˈhɪstri/', meaning: '历史；历史学；经历' },
        'hole': { phonetic: '/həʊl/', meaning: '洞；孔；坑' },
        'hope': { phonetic: '/həʊp/', meaning: '希望；期望；愿望' },
        'hour': { phonetic: '/ˈaʊə(r)/', meaning: '小时；时刻；钟头' },
        'humor': { phonetic: '/ˈhjuːmə(r)/', meaning: '幽默；幽默感；情绪' },
        'ice': { phonetic: '/aɪs/', meaning: '冰；冰块；冰淇淋' },
        'idea': { phonetic: '/aɪˈdɪə/', meaning: '主意；想法；概念' },
        'impulse': { phonetic: '/ˈɪmpʌls/', meaning: '冲动；脉冲；推动' },
        'increase': { phonetic: '/ɪnˈkriːs/', meaning: '增加；增长；增多' },
        'industry': { phonetic: '/ˈɪndəstri/', meaning: '工业；产业；勤奋' },
        'ink': { phonetic: '/ɪŋk/', meaning: '墨水；油墨' },
        'insect': { phonetic: '/ˈɪnsekt/', meaning: '昆虫；虫' },
        'instrument': { phonetic: '/ˈɪnstrəmənt/', meaning: '仪器；工具；乐器' },
        'insurance': { phonetic: '/ɪnˈʃʊərəns/', meaning: '保险；保险费；保险业' },
        'interest': { phonetic: '/ˈɪntrəst/', meaning: '兴趣；利益；利息' },
        'invention': { phonetic: '/ɪnˈvenʃn/', meaning: '发明；创造；虚构' },
        'iron': { phonetic: '/ˈaɪən/', meaning: '铁；熨斗；铁器' },
        'jelly': { phonetic: '/ˈdʒeli/', meaning: '果冻；果酱；胶状物' },
        'join': { phonetic: '/dʒɔɪn/', meaning: '加入；连接；参加' },
        'journey': { phonetic: '/ˈdʒɜːni/', meaning: '旅行；行程；历程' },
        'judge': { phonetic: '/dʒʌdʒ/', meaning: '法官；裁判；判断' },
        'jump': { phonetic: '/dʒʌmp/', meaning: '跳；跳跃；猛涨' },
        'kick': { phonetic: '/kɪk/', meaning: '踢；踹；踢腿' },
        'kiss': { phonetic: '/kɪs/', meaning: '吻；亲吻；轻触' },
        'knowledge': { phonetic: '/ˈnɒlɪdʒ/', meaning: '知识；学问；了解' },
        'land': { phonetic: '/lænd/', meaning: '陆地；土地；登陆' },
        'language': { phonetic: '/ˈlæŋɡwɪdʒ/', meaning: '语言；语言文字；表达能力' },
        'laugh': { phonetic: '/lɑːf/', meaning: '笑；笑声；发笑' },
        'law': { phonetic: '/lɔː/', meaning: '法律；法则；规律' },
        'lead': { phonetic: '/liːd/', meaning: '领导；引导；领先' },
        'learning': { phonetic: '/ˈlɜːnɪŋ/', meaning: '学习；学问；学识' },
        'leather': { phonetic: '/ˈleðə(r)/', meaning: '皮革；皮革制品' },
        'letter': { phonetic: '/ˈletə(r)/', meaning: '信；字母；函件' },
        'level': { phonetic: '/ˈlevl/', meaning: '水平；等级；高度' },
        'lift': { phonetic: '/lɪft/', meaning: '举起；电梯；搭便车' },
        'light': { phonetic: '/laɪt/', meaning: '光；光线；灯' },
        'limit': { phonetic: '/ˈlɪmɪt/', meaning: '限制；限度；界限' },
        'linen': { phonetic: '/ˈlɪnɪn/', meaning: '亚麻布；亚麻制品' },
        'liquid': { phonetic: '/ˈlɪkwɪd/', meaning: '液体；液态的' },
        'list': { phonetic: '/lɪst/', meaning: '列表；清单；目录' },
        'look': { phonetic: '/lʊk/', meaning: '看；瞧；看起来' },
        'loss': { phonetic: '/lɒs/', meaning: '损失；丧失；亏损' },
        'love': { phonetic: '/lʌv/', meaning: '爱；热爱；爱情' },
        'machine': { phonetic: '/məˈʃiːn/', meaning: '机器；机械；机构' },
        'man': { phonetic: '/mæn/', meaning: '男人；人类；人' },
        'manager': { phonetic: '/ˈmænɪdʒə(r)/', meaning: '经理；管理人；主管' },
        'mark': { phonetic: '/mɑːk/', meaning: '标记；痕迹；分数' },
        'market': { phonetic: '/ˈmɑːkɪt/', meaning: '市场；集市；行情' },
        'mass': { phonetic: '/mæs/', meaning: '大量；众多；质量' },
        'meal': { phonetic: '/miːl/', meaning: '一餐；饭食；膳食' },
        'measure': { phonetic: '/ˈmeʒə(r)/', meaning: '测量；衡量；措施' },
        'meat': { phonetic: '/miːt/', meaning: '肉；肉类；食用肉' },
        'meeting': { phonetic: '/ˈmiːtɪŋ/', meaning: '会议；会面；集会' },
        'memory': { phonetic: '/ˈmeməri/', meaning: '记忆；记忆力；回忆' },
        'metal': { phonetic: '/ˈmetl/', meaning: '金属；金属制品' },
        'middle': { phonetic: '/ˈmɪdl/', meaning: '中间；中部；当中' },
        'milk': { phonetic: '/mɪlk/', meaning: '牛奶；乳；乳汁' },
        'mind': { phonetic: '/maɪnd/', meaning: '头脑；精神；介意' },
        'mine': { phonetic: '/maɪn/', meaning: '矿；矿山；地雷' },
        'minute': { phonetic: '/ˈmɪnɪt/', meaning: '分钟；片刻；备忘录' },
        'mist': { phonetic: '/mɪst/', meaning: '薄雾；雾霭；水汽' },
        'money': { phonetic: '/ˈmʌni/', meaning: '钱；货币；财富' },
        'month': { phonetic: '/mʌnθ/', meaning: '月；月份；一个月的时间' },
        'morning': { phonetic: '/ˈmɔːnɪŋ/', meaning: '早晨；上午；清晨' },
        'mother': { phonetic: '/ˈmʌðə(r)/', meaning: '母亲；妈妈；根源' },
        'motion': { phonetic: '/ˈməʊʃn/', meaning: '运动；动作；手势' },
        'mountain': { phonetic: '/ˈmaʊntən/', meaning: '山；高山；山脉' },
        'move': { phonetic: '/muːv/', meaning: '移动；搬家；感动' },
        'music': { phonetic: '/ˈmjuːzɪk/', meaning: '音乐；乐曲；乐谱' },
        'name': { phonetic: '/neɪm/', meaning: '名字；名称；名声' },
        'nation': { phonetic: '/ˈneɪʃn/', meaning: '国家；民族；国民' },
        'need': { phonetic: '/niːd/', meaning: '需要；必需；需求' },
        'news': { phonetic: '/njuːz/', meaning: '新闻；消息；新闻报道' },
        'night': { phonetic: '/naɪt/', meaning: '夜晚；晚上；黑夜' },
        'noise': { phonetic: '/nɔɪz/', meaning: '噪音；声响；嘈杂声' },
        'note': { phonetic: '/nəʊt/', meaning: '笔记；便条；音符' },
        'number': { phonetic: '/ˈnʌmbə(r)/', meaning: '数字；号码；数量' },
        'observation': { phonetic: '/ˌɒbzəˈveɪʃn/', meaning: '观察；观测；监视' },
        'offer': { phonetic: '/ˈɒfə(r)/', meaning: '提供；出价；提议' },
        'oil': { phonetic: '/ɔɪl/', meaning: '油；石油；油画颜料' },
        'operation': { phonetic: '/ˌɒpəˈreɪʃn/', meaning: '操作；运转；手术' },
        'opinion': { phonetic: '/əˈpɪnjən/', meaning: '意见；看法；主张' },
        'order': { phonetic: '/ˈɔːdə(r)/', meaning: '顺序；秩序；命令' },
        'organization': { phonetic: '/ˌɔːɡənaɪˈzeɪʃn/', meaning: '组织；机构；团体' },
        'ornament': { phonetic: '/ˈɔːnəmənt/', meaning: '装饰；装饰物；点缀' },
        'owner': { phonetic: '/ˈəʊnə(r)/', meaning: '所有者；物主；主人' },
        'page': { phonetic: '/peɪdʒ/', meaning: '页；页面；版面' },
        'pain': { phonetic: '/peɪn/', meaning: '疼痛；痛苦；苦恼' },
        'paint': { phonetic: '/peɪnt/', meaning: '油漆；颜料；绘画' },
        'paper': { phonetic: '/ˈpeɪpə(r)/', meaning: '纸；纸张；文件' },
        'part': { phonetic: '/pɑːt/', meaning: '部分；角色；零件' },
        'paste': { phonetic: '/peɪst/', meaning: '糊；浆糊；粘贴' },
        'payment': { phonetic: '/ˈpeɪmənt/', meaning: '付款；支付；报酬' },
        'peace': { phonetic: '/piːs/', meaning: '和平；平静；安宁' },
        'person': { phonetic: '/ˈpɜːsn/', meaning: '人；个人；人称' },
        'place': { phonetic: '/pleɪs/', meaning: '地方；地点；位置' },
        'plant': { phonetic: '/plɑːnt/', meaning: '植物；工厂；设备' },
        'play': { phonetic: '/pleɪ/', meaning: '玩耍；游戏；演奏' },
        'pleasure': { phonetic: '/ˈpleʒə(r)/', meaning: '快乐；愉快；乐事' },
        'point': { phonetic: '/pɔɪnt/', meaning: '点；要点；观点' },
        'poison': { phonetic: '/ˈpɔɪzn/', meaning: '毒药；毒物；毒害' },
        'polish': { phonetic: '/ˈpɒlɪʃ/', meaning: '擦亮；磨光；抛光' },
        'porter': { phonetic: '/ˈpɔːtə(r)/', meaning: '搬运工；门房；服务员' },
        'position': { phonetic: '/pəˈzɪʃn/', meaning: '位置；职位；姿势' },
        'powder': { phonetic: '/ˈpaʊdə(r)/', meaning: '粉末；粉；火药' },
        'power': { phonetic: '/ˈpaʊə(r)/', meaning: '力量；权力；功率' },
        'price': { phonetic: '/praɪs/', meaning: '价格；价钱；代价' },
        'process': { phonetic: '/ˈprəʊses/', meaning: '过程；进程；工序' },
        'produce': { phonetic: '/prəˈdjuːs/', meaning: '生产；制造；产生' },
        'profit': { phonetic: '/ˈprɒfɪt/', meaning: '利润；收益；得益' },
        'property': { phonetic: '/ˈprɒpəti/', meaning: '财产；属性；性质' },
        'prose': { phonetic: '/prəʊz/', meaning: '散文；平铺直叙' },
        'protest': { phonetic: '/ˈprəʊtest/', meaning: '抗议；反对；申明' },
        'pull': { phonetic: '/pʊl/', meaning: '拉；拖；拔' },
        'punishment': { phonetic: '/ˈpʌnɪʃmənt/', meaning: '惩罚；处罚；刑罚' },
        'purpose': { phonetic: '/ˈpɜːpəs/', meaning: '目的；意图；用途' },
        'push': { phonetic: '/pʊʃ/', meaning: '推；推动；逼迫' },
        'quality': { phonetic: '/ˈkwɒləti/', meaning: '质量；品质；特性' },
        'question': { phonetic: '/ˈkwestʃən/', meaning: '问题；疑问；询问' },
        'rain': { phonetic: '/reɪn/', meaning: '雨；雨水；下雨' },
        'range': { phonetic: '/reɪndʒ/', meaning: '范围；幅度；山脉' },
        'rate': { phonetic: '/reɪt/', meaning: '比率；速度；价格' },
        'ray': { phonetic: '/reɪ/', meaning: '光线；射线；光束' },
        'reaction': { phonetic: '/riˈækʃn/', meaning: '反应；反作用；化学反应' },
        'reading': { phonetic: '/ˈriːdɪŋ/', meaning: '阅读；朗读；读数' },
        'reason': { phonetic: '/ˈriːzn/', meaning: '理由；原因；理性' },
        'record': { phonetic: '/ˈrekɔːd/', meaning: '记录；唱片；履历' },
        'regret': { phonetic: '/rɪˈɡret/', meaning: '后悔；遗憾；惋惜' },
        'relation': { phonetic: '/rɪˈleɪʃn/', meaning: '关系；联系；亲属' },
        'religion': { phonetic: '/rɪˈlɪdʒən/', meaning: '宗教；信仰；教派' },
        'representative': { phonetic: '/ˌreprɪˈzentətɪv/', meaning: '代表；代理人；典型' },
        'request': { phonetic: '/rɪˈkwest/', meaning: '请求；要求；申请' },
        'respect': { phonetic: '/rɪˈspekt/', meaning: '尊敬；尊重；方面' },
        'rest': { phonetic: '/rest/', meaning: '休息；剩余部分；静止' },
        'reward': { phonetic: '/rɪˈwɔːd/', meaning: '报酬；奖励；报答' },
        'rhythm': { phonetic: '/ˈrɪðəm/', meaning: '节奏；韵律；律动' },
        'rice': { phonetic: '/raɪs/', meaning: '稻；大米；米饭' },
        'river': { phonetic: '/ˈrɪvə(r)/', meaning: '河；河流；江河' },
        'road': { phonetic: '/rəʊd/', meaning: '路；道路；公路' },
        'roll': { phonetic: '/rəʊl/', meaning: '滚动；卷；名册' },
        'room': { phonetic: '/ruːm/', meaning: '房间；空间；余地' },
        'rub': { phonetic: '/rʌb/', meaning: '擦；摩擦；揉搓' },
        'rule': { phonetic: '/ruːl/', meaning: '规则；统治；规定' },
        'run': { phonetic: '/rʌn/', meaning: '跑；奔跑；运行' },
        'salt': { phonetic: '/sɔːlt/', meaning: '盐；食盐；咸' },
        'sand': { phonetic: '/sænd/', meaning: '沙；沙子；沙滩' },
        'scale': { phonetic: '/skeɪl/', meaning: '规模；比例；刻度' },
        'science': { phonetic: '/ˈsaɪəns/', meaning: '科学；学科；自然科学' },
        'sea': { phonetic: '/siː/', meaning: '海；海洋；海水' },
        'seat': { phonetic: '/siːt/', meaning: '座位；座；席位' },
        'secretary': { phonetic: '/ˈsekrətri/', meaning: '秘书；书记；部长' },
        'selection': { phonetic: '/sɪˈlekʃn/', meaning: '选择；挑选；选集' },
        'self': { phonetic: '/self/', meaning: '自己；自我；本身' },
        'sense': { phonetic: '/sens/', meaning: '感觉；感官；意义' },
        'servant': { phonetic: '/ˈsɜːvənt/', meaning: '仆人；佣人；雇员' },
        'sex': { phonetic: '/seks/', meaning: '性；性别；性行为' },
        'shade': { phonetic: '/ʃeɪd/', meaning: '阴凉处；阴影；灯罩' },
        'shake': { phonetic: '/ʃeɪk/', meaning: '摇动；震动；颤抖' },
        'shame': { phonetic: '/ʃeɪm/', meaning: '羞愧；羞耻；遗憾' },
        'shock': { phonetic: '/ʃɒk/', meaning: '震惊；震动；休克' },
        'side': { phonetic: '/saɪd/', meaning: '边；侧面；方面' },
        'sign': { phonetic: '/saɪn/', meaning: '符号；标志；迹象' },
        'silk': { phonetic: '/sɪlk/', meaning: '丝；丝绸；蚕丝' },
        'silver': { phonetic: '/ˈsɪlvə(r)/', meaning: '银；银子；银色' },
        'sister': { phonetic: '/ˈsɪstə(r)/', meaning: '姐妹；姐姐；妹妹' },
        'size': { phonetic: '/saɪz/', meaning: '大小；尺寸；规模' },
        'sky': { phonetic: '/skaɪ/', meaning: '天空；天' },
        'sleep': { phonetic: '/sliːp/', meaning: '睡眠；睡觉；睡' },
        'slip': { phonetic: '/slɪp/', meaning: '滑倒；滑；溜走' },
        'slope': { phonetic: '/sləʊp/', meaning: '斜坡；斜面；倾斜' },
        'smash': { phonetic: '/smæʃ/', meaning: '打碎；粉碎；猛撞' },
        'smell': { phonetic: '/smel/', meaning: '气味；嗅觉；闻' },
        'smile': { phonetic: '/smaɪl/', meaning: '微笑；笑容；喜色' },
        'smoke': { phonetic: '/sməʊk/', meaning: '烟；烟雾；抽烟' },
        'sneeze': { phonetic: '/sniːz/', meaning: '打喷嚏；喷嚏' },
        'snow': { phonetic: '/snəʊ/', meaning: '雪；下雪；积雪' },
        'soap': { phonetic: '/səʊp/', meaning: '肥皂；香皂' },
        'society': { phonetic: '/səˈsaɪəti/', meaning: '社会；社团；协会' },
        'son': { phonetic: '/sʌn/', meaning: '儿子；孩子' },
        'song': { phonetic: '/sɒŋ/', meaning: '歌；歌曲；歌声' },
        'sort': { phonetic: '/sɔːt/', meaning: '种类；类别；排序' },
        'sound': { phonetic: '/saʊnd/', meaning: '声音；声响；听起来' },
        'soup': { phonetic: '/suːp/', meaning: '汤；羹' },
        'space': { phonetic: '/speɪs/', meaning: '空间；太空；空地' },
        'stage': { phonetic: '/steɪdʒ/', meaning: '舞台；阶段；时期' },
        'start': { phonetic: '/stɑːt/', meaning: '开始；出发；启动' },
        'statement': { phonetic: '/ˈsteɪtmənt/', meaning: '陈述；声明；报告' },
        'steam': { phonetic: '/stiːm/', meaning: '蒸汽；水蒸气；水汽' },
        'steel': { phonetic: '/stiːl/', meaning: '钢；钢铁；钢制的' },
        'step': { phonetic: '/step/', meaning: '步；脚步；步骤' },
        'stitch': { phonetic: '/stɪtʃ/', meaning: '一针；缝法；缝线' },
        'stone': { phonetic: '/stəʊn/', meaning: '石头；石块；宝石' },
        'stop': { phonetic: '/stɒp/', meaning: '停止；停下；阻止' },
        'story': { phonetic: '/ˈstɔːri/', meaning: '故事；小说；传说' },
        'stretch': { phonetic: '/stretʃ/', meaning: '伸展；拉长；延伸' },
        'structure': { phonetic: '/ˈstrʌktʃə(r)/', meaning: '结构；构造；建筑物' },
        'substance': { phonetic: '/ˈsʌbstəns/', meaning: '物质；实质；本质' },
        'sugar': { phonetic: '/ˈʃʊɡə(r)/', meaning: '糖；食糖；蔗糖' },
        'suggestion': { phonetic: '/səˈdʒestʃən/', meaning: '建议；意见；暗示' },
        'summer': { phonetic: '/ˈsʌmə(r)/', meaning: '夏天；夏季' },
        'support': { phonetic: '/səˈpɔːt/', meaning: '支持；支撑；帮助' },
        'surprise': { phonetic: '/səˈpraɪz/', meaning: '惊奇；惊讶；意外' },
        'swim': { phonetic: '/swɪm/', meaning: '游泳；游动；浸泡' },
        'system': { phonetic: '/ˈsɪstəm/', meaning: '系统；体系；制度' },
        'talk': { phonetic: '/tɔːk/', meaning: '谈话；交谈；演讲' },
        'taste': { phonetic: '/teɪst/', meaning: '味道；味觉；品尝' },
        'tax': { phonetic: '/tæks/', meaning: '税；税款；征税' },
        'teaching': { phonetic: '/ˈtiːtʃɪŋ/', meaning: '教学；教导；教义' },
        'tendency': { phonetic: '/ˈtendənsi/', meaning: '倾向；趋势；趋向' },
        'test': { phonetic: '/test/', meaning: '测试；试验；考验' },
        'theory': { phonetic: '/ˈθɪəri/', meaning: '理论；学说；原理' },
        'thing': { phonetic: '/θɪŋ/', meaning: '东西；事物；事情' },
        'thought': { phonetic: '/θɔːt/', meaning: '思想；思考；想法' },
        'thunder': { phonetic: '/ˈθʌndə(r)/', meaning: '雷；雷声；雷鸣' },
        'time': { phonetic: '/taɪm/', meaning: '时间；时刻；次' },
        'tin': { phonetic: '/tɪn/', meaning: '锡；罐头；马口铁' },
        'top': { phonetic: '/tɒp/', meaning: '顶部；顶端；上面' },
        'touch': { phonetic: '/tʌtʃ/', meaning: '触摸；接触；碰' },
        'trade': { phonetic: '/treɪd/', meaning: '贸易；交易；行业' },
        'transport': { phonetic: '/trænˈspɔːt/', meaning: '运输；运送；交通工具' },
        'trick': { phonetic: '/trɪk/', meaning: '诡计；把戏；诀窍' },
        'trouble': { phonetic: '/ˈtrʌbl/', meaning: '麻烦；烦恼；故障' },
        'turn': { phonetic: '/tɜːn/', meaning: '转动；旋转；转弯' },
        'twist': { phonetic: '/twɪst/', meaning: '扭曲；拧；扭转' },
        'unit': { phonetic: '/ˈjuːnɪt/', meaning: '单位；单元；部件' },
        'use': { phonetic: '/juːz/', meaning: '使用；利用；用途' },
        'value': { phonetic: '/ˈvæljuː/', meaning: '价值；价格；重要性' },
        'verse': { phonetic: '/vɜːs/', meaning: '诗；韵文；诗句' },
        'vessel': { phonetic: '/ˈvesl/', meaning: '船；容器；血管' },
        'view': { phonetic: '/vjuː/', meaning: '看法；视野；景色' },
        'voice': { phonetic: '/vɔɪs/', meaning: '声音；嗓音；发言权' },
        'walk': { phonetic: '/wɔːk/', meaning: '走；步行；散步' },
        'war': { phonetic: '/wɔː(r)/', meaning: '战争；战争状态；斗争' },
        'wash': { phonetic: '/wɒʃ/', meaning: '洗；洗涤；冲洗' },
        'waste': { phonetic: '/weɪst/', meaning: '浪费；废物；废料' },
        'water': { phonetic: '/ˈwɔːtə(r)/', meaning: '水；雨水；水域' },
        'wave': { phonetic: '/weɪv/', meaning: '波浪；波动；挥手' },
        'wax': { phonetic: '/wæks/', meaning: '蜡；蜂蜡；打蜡' },
        'way': { phonetic: '/weɪ/', meaning: '路；道路；方法' },
        'weather': { phonetic: '/ˈweðə(r)/', meaning: '天气；气象；气候' },
        'week': { phonetic: '/wiːk/', meaning: '星期；周；礼拜' },
        'weight': { phonetic: '/weɪt/', meaning: '重量；体重；重力' },
        'wind': { phonetic: '/wɪnd/', meaning: '风；气流；气息' },
        'wine': { phonetic: '/waɪn/', meaning: '葡萄酒；酒；果酒' },
        'winter': { phonetic: '/ˈwɪntə(r)/', meaning: '冬天；冬季' },
        'woman': { phonetic: '/ˈwʊmən/', meaning: '女人；妇女；成年女子' },
        'wood': { phonetic: '/wʊd/', meaning: '木；木材；树林' },
        'wool': { phonetic: '/wʊl/', meaning: '羊毛；毛线；毛料' },
        'word': { phonetic: '/wɜːd/', meaning: '词；单词；话语' },
        'work': { phonetic: '/wɜːk/', meaning: '工作；劳动；著作' },
        'wound': { phonetic: '/wuːnd/', meaning: '伤口；创伤；伤害' },
        'writing': { phonetic: '/ˈraɪtɪŋ/', meaning: '写作；书写；文字' },
        'year': { phonetic: '/jɪə(r)/', meaning: '年；年份；年纪' },
        // Things — Picturable
        'angle': { phonetic: '/ˈæŋɡl/', meaning: '角；角度' },
        'ant': { phonetic: '/ænt/', meaning: '蚂蚁' },
        'apple': { phonetic: '/ˈæpl/', meaning: '苹果' },
        'arch': { phonetic: '/ɑːtʃ/', meaning: '拱门；拱' },
        'arm': { phonetic: '/ɑːm/', meaning: '手臂；胳膊' },
        'army': { phonetic: '/ˈɑːmi/', meaning: '军队；陆军' },
        'baby': { phonetic: '/ˈbeɪbi/', meaning: '婴儿；宝贝' },
        'bag': { phonetic: '/bæɡ/', meaning: '袋；包' },
        'ball': { phonetic: '/bɔːl/', meaning: '球；舞会' },
        'band': { phonetic: '/bænd/', meaning: '乐队；带；群' },
        'basin': { phonetic: '/ˈbeɪsn/', meaning: '盆；水盆' },
        'basket': { phonetic: '/ˈbɑːskɪt/', meaning: '篮；筐；篓' },
        'bath': { phonetic: '/bɑːθ/', meaning: '洗澡；浴缸' },
        'bed': { phonetic: '/bed/', meaning: '床；床铺' },
        'bee': { phonetic: '/biː/', meaning: '蜜蜂' },
        'bell': { phonetic: '/bel/', meaning: '铃；钟' },
        'berry': { phonetic: '/ˈberi/', meaning: '浆果' },
        'bird': { phonetic: '/bɜːd/', meaning: '鸟；禽' },
        'blade': { phonetic: '/bleɪd/', meaning: '刀片；刀刃' },
        'board': { phonetic: '/bɔːd/', meaning: '板；木板；董事会' },
        'boat': { phonetic: '/bəʊt/', meaning: '船；小船' },
        'bone': { phonetic: '/bəʊn/', meaning: '骨；骨头' },
        'book': { phonetic: '/bʊk/', meaning: '书；书籍' },
        'boot': { phonetic: '/buːt/', meaning: '靴；靴子' },
        'bottle': { phonetic: '/ˈbɒtl/', meaning: '瓶子；一瓶' },
        'box': { phonetic: '/bɒks/', meaning: '箱；盒；方框' },
        'boy': { phonetic: '/bɔɪ/', meaning: '男孩；少年' },
        'brain': { phonetic: '/breɪn/', meaning: '脑；大脑；头脑' },
        'brake': { phonetic: '/breɪk/', meaning: '闸；刹车；制动器' },
        'branch': { phonetic: '/brɑːntʃ/', meaning: '树枝；分支；分店' },
        'brick': { phonetic: '/brɪk/', meaning: '砖；砖块' },
        'bridge': { phonetic: '/brɪdʒ/', meaning: '桥；桥梁' },
        'brush': { phonetic: '/brʌʃ/', meaning: '刷子；画笔；刷' },
        'bucket': { phonetic: '/ˈbʌkɪt/', meaning: '桶；水桶' },
        'bulb': { phonetic: '/bʌlb/', meaning: '灯泡；球茎' },
        'button': { phonetic: '/ˈbʌtn/', meaning: '纽扣；按钮' },
        'cake': { phonetic: '/keɪk/', meaning: '蛋糕；糕饼' },
        'camera': { phonetic: '/ˈkæmərə/', meaning: '照相机；摄影机' },
        'card': { phonetic: '/kɑːd/', meaning: '卡片；纸牌；名片' },
        'cart': { phonetic: '/kɑːt/', meaning: '推车；马车' },
        'carriage': { phonetic: '/ˈkærɪdʒ/', meaning: '车厢；马车' },
        'cat': { phonetic: '/kæt/', meaning: '猫；猫科动物' },
        'chain': { phonetic: '/tʃeɪn/', meaning: '链；链条；连锁' },
        'cheese': { phonetic: '/tʃiːz/', meaning: '奶酪；干酪' },
        'chest': { phonetic: '/tʃest/', meaning: '胸部；胸膛；箱子' },
        'chin': { phonetic: '/tʃɪn/', meaning: '下巴；颏' },
        'church': { phonetic: '/tʃɜːtʃ/', meaning: '教堂；教会' },
        'circle': { phonetic: '/ˈsɜːkl/', meaning: '圆；圆圈；圆形' },
        'clock': { phonetic: '/klɒk/', meaning: '钟；时钟' },
        'cloud': { phonetic: '/klaʊd/', meaning: '云；云朵' },
        'coat': { phonetic: '/kəʊt/', meaning: '外套；大衣；涂层' },
        'collar': { phonetic: '/ˈkɒlə(r)/', meaning: '衣领；项圈' },
        'comb': { phonetic: '/kəʊm/', meaning: '梳子；梳理' },
        'cord': { phonetic: '/kɔːd/', meaning: '绳；索；线' },
        'cow': { phonetic: '/kaʊ/', meaning: '母牛；奶牛' },
        'cup': { phonetic: '/kʌp/', meaning: '杯子；一杯' },
        'curtain': { phonetic: '/ˈkɜːtn/', meaning: '窗帘；幕' },
        'cushion': { phonetic: '/ˈkʊʃn/', meaning: '垫子；坐垫' },
        'dog': { phonetic: '/dɒɡ/', meaning: '狗；犬' },
        'door': { phonetic: '/dɔː(r)/', meaning: '门；门户' },
        'drain': { phonetic: '/dreɪn/', meaning: '排水；下水道；消耗' },
        'drawer': { phonetic: '/drɔː(r)/', meaning: '抽屉' },
        'dress': { phonetic: '/dres/', meaning: '连衣裙；服装' },
        'drop': { phonetic: '/drɒp/', meaning: '滴；落下；下降' },
        'ear': { phonetic: '/ɪə(r)/', meaning: '耳朵；耳状物' },
        'egg': { phonetic: '/eɡ/', meaning: '蛋；卵；鸡蛋' },
        'engine': { phonetic: '/ˈendʒɪn/', meaning: '发动机；引擎；火车头' },
        'eye': { phonetic: '/aɪ/', meaning: '眼睛；眼光；视力' },
        'face': { phonetic: '/feɪs/', meaning: '脸；面孔；表面' },
        'farm': { phonetic: '/fɑːm/', meaning: '农场；饲养场' },
        'feather': { phonetic: '/ˈfeðə(r)/', meaning: '羽毛' },
        'finger': { phonetic: '/ˈfɪŋɡə(r)/', meaning: '手指；指针' },
        'fish': { phonetic: '/fɪʃ/', meaning: '鱼；鱼类' },
        'flag': { phonetic: '/flæɡ/', meaning: '旗；旗帜；标记' },
        'floor': { phonetic: '/flɔː(r)/', meaning: '地板；楼层' },
        'fly': { phonetic: '/flaɪ/', meaning: '飞；苍蝇；飞行' },
        'foot': { phonetic: '/fʊt/', meaning: '脚；足；英尺' },
        'fork': { phonetic: '/fɔːk/', meaning: '叉；餐叉；叉子' },
        'fowl': { phonetic: '/faʊl/', meaning: '家禽；禽；鸟' },
        'frame': { phonetic: '/freɪm/', meaning: '框架；构架；结构' },
        'garden': { phonetic: '/ˈɡɑːdn/', meaning: '花园；菜园；园圃' },
        'girl': { phonetic: '/ɡɜːl/', meaning: '女孩；姑娘；女儿' },
        'glove': { phonetic: '/ɡlʌv/', meaning: '手套' },
        'goat': { phonetic: '/ɡəʊt/', meaning: '山羊' },
        'gun': { phonetic: '/ɡʌn/', meaning: '枪；炮；枪炮' },
        'hair': { phonetic: '/heə(r)/', meaning: '头发；毛发' },
        'hammer': { phonetic: '/ˈhæmə(r)/', meaning: '锤子；榔头；锤击' },
        'hand': { phonetic: '/hænd/', meaning: '手；手掌；指针' },
        'hat': { phonetic: '/hæt/', meaning: '帽子' },
        'head': { phonetic: '/hed/', meaning: '头；头部；头脑' },
        'heart': { phonetic: '/hɑːt/', meaning: '心；心脏；中心' },
        'hook': { phonetic: '/hʊk/', meaning: '钩；挂钩；钩子' },
        'horn': { phonetic: '/hɔːn/', meaning: '角；号角；喇叭' },
        'horse': { phonetic: '/hɔːs/', meaning: '马；骑马' },
        'hospital': { phonetic: '/ˈhɒspɪtl/', meaning: '医院' },
        'house': { phonetic: '/haʊs/', meaning: '房屋；房子；住宅' },
        'island': { phonetic: '/ˈaɪlənd/', meaning: '岛；岛屿' },
        'jewel': { phonetic: '/ˈdʒuːəl/', meaning: '宝石；珠宝' },
        'kettle': { phonetic: '/ˈketl/', meaning: '水壶' },
        'key': { phonetic: '/kiː/', meaning: '钥匙；键；关键' },
        'knee': { phonetic: '/niː/', meaning: '膝盖；膝' },
        'knife': { phonetic: '/naɪf/', meaning: '刀；小刀；菜刀' },
        'knot': { phonetic: '/nɒt/', meaning: '结；绳结；节' },
        'leaf': { phonetic: '/liːf/', meaning: '叶；叶子；书页' },
        'leg': { phonetic: '/leɡ/', meaning: '腿；腿部；腿脚' },
        'library': { phonetic: '/ˈlaɪbrəri/', meaning: '图书馆；图书室' },
        'line': { phonetic: '/laɪn/', meaning: '线；线条；界线' },
        'lip': { phonetic: '/lɪp/', meaning: '嘴唇；唇' },
        'lock': { phonetic: '/lɒk/', meaning: '锁；水闸；一绺' },
        'map': { phonetic: '/mæp/', meaning: '地图；图；天体图' },
        'match': { phonetic: '/mætʃ/', meaning: '比赛；火柴；相配' },
        'monkey': { phonetic: '/ˈmʌŋki/', meaning: '猴子；猴' },
        'moon': { phonetic: '/muːn/', meaning: '月亮；月球' },
        'mouth': { phonetic: '/maʊθ/', meaning: '口；嘴；河口' },
        'muscle': { phonetic: '/ˈmʌsl/', meaning: '肌肉；体力' },
        'nail': { phonetic: '/neɪl/', meaning: '钉；钉子；指甲' },
        'neck': { phonetic: '/nek/', meaning: '颈；脖子' },
        'needle': { phonetic: '/ˈniːdl/', meaning: '针；指针；针叶' },
        'nerve': { phonetic: '/nɜːv/', meaning: '神经；神经紧张；勇气' },
        'net': { phonetic: '/net/', meaning: '网；网状物；净' },
        'nose': { phonetic: '/nəʊz/', meaning: '鼻子；鼻；鼻状物' },
        'nut': { phonetic: '/nʌt/', meaning: '坚果；螺母；螺帽' },
        'office': { phonetic: '/ˈɒfɪs/', meaning: '办公室；办事处；职位' },
        'orange': { phonetic: '/ˈɒrɪndʒ/', meaning: '橙；橙色；橙色的' },
        'oven': { phonetic: '/ˈʌvn/', meaning: '烤箱；炉；灶' },
        'parcel': { phonetic: '/ˈpɑːsl/', meaning: '包裹；小包' },
        'pen': { phonetic: '/pen/', meaning: '笔；钢笔；围栏' },
        'pencil': { phonetic: '/ˈpensl/', meaning: '铅笔' },
        'picture': { phonetic: '/ˈpɪktʃə(r)/', meaning: '画；图画；照片' },
        'pig': { phonetic: '/pɪɡ/', meaning: '猪；猪科动物' },
        'pin': { phonetic: '/pɪn/', meaning: '针；大头针；别针' },
        'pipe': { phonetic: '/paɪp/', meaning: '管；导管；烟斗' },
        'plane': { phonetic: '/pleɪn/', meaning: '飞机；平面；刨子' },
        'plate': { phonetic: '/pleɪt/', meaning: '盘；盘子；板' },
        'plough': { phonetic: '/plaʊ/', meaning: '犁；耕' },
        'pocket': { phonetic: '/ˈpɒkɪt/', meaning: '口袋；兜；袖珍的' },
        'pot': { phonetic: '/pɒt/', meaning: '锅；罐；壶' },
        'potato': { phonetic: '/pəˈteɪtəʊ/', meaning: '土豆；马铃薯' },
        'prison': { phonetic: '/ˈprɪzn/', meaning: '监狱；看守所' },
        'pump': { phonetic: '/pʌmp/', meaning: '泵；抽水机；打气筒' },
        'rail': { phonetic: '/reɪl/', meaning: '栏杆；扶手；铁路' },
        'rat': { phonetic: '/ræt/', meaning: '鼠；耗子；卑鄙小人' },
        'receipt': { phonetic: '/rɪˈsiːt/', meaning: '收据；收条；收到' },
        'ring': { phonetic: '/rɪŋ/', meaning: '环；戒指；铃声' },
        'rod': { phonetic: '/rɒd/', meaning: '杆；棒；棍' },
        'roof': { phonetic: '/ruːf/', meaning: '屋顶；顶部' },
        'root': { phonetic: '/ruːt/', meaning: '根；根部；根源' },
        'sail': { phonetic: '/seɪl/', meaning: '帆；航行；帆状物' },
        'school': { phonetic: '/skuːl/', meaning: '学校；学院；学派' },
        'scissors': { phonetic: '/ˈsɪzəz/', meaning: '剪刀；剪子' },
        'screw': { phonetic: '/skruː/', meaning: '螺丝；螺钉；拧紧' },
        'seed': { phonetic: '/siːd/', meaning: '种子；籽；萌芽' },
        'sheep': { phonetic: '/ʃiːp/', meaning: '羊；绵羊；驯顺的人' },
        'shelf': { phonetic: '/ʃelf/', meaning: '架子；搁板；隔板' },
        'ship': { phonetic: '/ʃɪp/', meaning: '船；舰；海轮' },
        'shirt': { phonetic: '/ʃɜːt/', meaning: '衬衫；衬衣' },
        'shoe': { phonetic: '/ʃuː/', meaning: '鞋；鞋子' },
        'skin': { phonetic: '/skɪn/', meaning: '皮肤；皮；兽皮' },
        'skirt': { phonetic: '/skɜːt/', meaning: '裙子；女裙；边缘' },
        'snake': { phonetic: '/sneɪk/', meaning: '蛇；阴险的人' },
        'sock': { phonetic: '/sɒk/', meaning: '袜子；短袜' },
        'spade': { phonetic: '/speɪd/', meaning: '铲；铁锹；纸牌中的黑桃' },
        'sponge': { phonetic: '/spʌndʒ/', meaning: '海绵；海绵状物' },
        'spoon': { phonetic: '/spuːn/', meaning: '匙；调羹；勺子' },
        'spring': { phonetic: '/sprɪŋ/', meaning: '春天；春季；弹簧' },
        'square': { phonetic: '/skweə(r)/', meaning: '正方形；广场；平方' },
        'stamp': { phonetic: '/stæmp/', meaning: '邮票；印章；跺脚' },
        'star': { phonetic: '/stɑː(r)/', meaning: '星；恒星；明星' },
        'station': { phonetic: '/ˈsteɪʃn/', meaning: '站；车站；位置' },
        'stem': { phonetic: '/stem/', meaning: '茎；干；梗' },
        'stick': { phonetic: '/stɪk/', meaning: '棍；棒；枝条' },
        'store': { phonetic: '/stɔː(r)/', meaning: '商店；仓库；存储' },
        'street': { phonetic: '/striːt/', meaning: '街；街道；马路' },
        'string': { phonetic: '/strɪŋ/', meaning: '线；弦；串' },
        'sun': { phonetic: '/sʌn/', meaning: '太阳；阳光；恒星' },
        'table': { phonetic: '/ˈteɪbl/', meaning: '桌子；台子；表格' },
        'tail': { phonetic: '/teɪl/', meaning: '尾巴；尾部；末尾' },
        'thread': { phonetic: '/θred/', meaning: '线；线索；思路' },
        'throat': { phonetic: '/θrəʊt/', meaning: '喉咙；咽喉；嗓音' },
        'thumb': { phonetic: '/θʌm/', meaning: '拇指；大拇哥' },
        'ticket': { phonetic: '/ˈtɪkɪt/', meaning: '票；车票；入场券' },
        'toe': { phonetic: '/təʊ/', meaning: '脚趾；足尖' },
        'tongue': { phonetic: '/tʌŋ/', meaning: '舌；舌头；语言' },
        'tooth': { phonetic: '/tuːθ/', meaning: '牙；牙齿；齿' },
        'town': { phonetic: '/taʊn/', meaning: '城；城镇；市镇' },
        'train': { phonetic: '/treɪn/', meaning: '火车；列车；训练' },
        'tray': { phonetic: '/treɪ/', meaning: '盘；托盘；浅盘' },
        'tree': { phonetic: '/triː/', meaning: '树；树木；乔木' },
        'trousers': { phonetic: '/ˈtraʊzəz/', meaning: '裤子；长裤' },
        'umbrella': { phonetic: '/ʌmˈbrelə/', meaning: '伞；雨伞；阳伞' },
        'wall': { phonetic: '/wɔːl/', meaning: '墙；墙壁；围墙' },
        'watch': { phonetic: '/wɒtʃ/', meaning: '手表；观看；注视' },
        'wheel': { phonetic: '/wiːl/', meaning: '轮；轮子；车轮' },
        'whip': { phonetic: '/wɪp/', meaning: '鞭子；抽打；鞭策' },
        'whistle': { phonetic: '/ˈwɪsl/', meaning: '口哨；哨子；吹口哨' },
        'window': { phonetic: '/ˈwɪndəʊ/', meaning: '窗；窗户；窗口' },
        'wing': { phonetic: '/wɪŋ/', meaning: '翅膀；翼；翅膀状物' },
        'wire': { phonetic: '/ˈwaɪə(r)/', meaning: '金属丝；电线；电报' },
        'worm': { phonetic: '/wɜːm/', meaning: '蠕虫；蚯蚓；小人物' },
        // Qualities
        'able': { phonetic: '/ˈeɪbl/', meaning: '能够；有能力的' },
        'acid': { phonetic: '/ˈæsɪd/', meaning: '酸的；酸性的；尖刻的' },
        'angry': { phonetic: '/ˈæŋɡri/', meaning: '愤怒的；生气的' },
        'beautiful': { phonetic: '/ˈbjuːtɪfl/', meaning: '美丽的；漂亮的' },
        'black': { phonetic: '/blæk/', meaning: '黑色的；黑的' },
        'blue': { phonetic: '/bluː/', meaning: '蓝色的；忧郁的' },
        'boiling': { phonetic: '/ˈbɔɪlɪŋ/', meaning: '沸腾的；极热的' },
        'bright': { phonetic: '/braɪt/', meaning: '明亮的；聪明的' },
        'broken': { phonetic: '/ˈbrəʊkən/', meaning: '破碎的；损坏的' },
        'brown': { phonetic: '/braʊn/', meaning: '棕色的；褐色的' },
        'cheap': { phonetic: '/tʃiːp/', meaning: '便宜的；廉价的' },
        'chemical': { phonetic: '/ˈkemɪkl/', meaning: '化学的；化学制品' },
        'chief': { phonetic: '/tʃiːf/', meaning: '主要的；首要的；首领' },
        'clean': { phonetic: '/kliːn/', meaning: '干净的；清洁的；打扫' },
        'clear': { phonetic: '/klɪə(r)/', meaning: '清晰的；清楚的；清除' },
        'common': { phonetic: '/ˈkɒmən/', meaning: '共同的；常见的；普通的' },
        'complex': { phonetic: '/ˈkɒmpleks/', meaning: '复杂的；复合的' },
        'conscious': { phonetic: '/ˈkɒnʃəs/', meaning: '意识到的；有知觉的' },
        'cut': { phonetic: '/kʌt/', meaning: '切；割；剪；砍' },
        'deep': { phonetic: '/diːp/', meaning: '深的；深厚的；纵深的' },
        'dependent': { phonetic: '/dɪˈpendənt/', meaning: '依赖的；依靠的' },
        'double': { phonetic: '/ˈdʌbl/', meaning: '双的；双重的；加倍' },
        'dry': { phonetic: '/draɪ/', meaning: '干的；干燥的；弄干' },
        'early': { phonetic: '/ˈɜːli/', meaning: '早的；早期的；提前' },
        'elastic': { phonetic: '/ɪˈlæstɪk/', meaning: '有弹性的；灵活的' },
        'electric': { phonetic: '/ɪˈlektrɪk/', meaning: '电的；电动的' },
        'equal': { phonetic: '/ˈiːkwəl/', meaning: '相等的；平等的；平等' },
        'fat': { phonetic: '/fæt/', meaning: '肥胖的；胖的；脂肪' },
        'fertile': { phonetic: '/ˈfɜːtaɪl/', meaning: '肥沃的；富饶的；多产的' },
        'first': { phonetic: '/fɜːst/', meaning: '第一的；最早的；首先' },
        'fixed': { phonetic: '/fɪkst/', meaning: '固定的；确定的' },
        'flat': { phonetic: '/flæt/', meaning: '平的；平坦的；公寓' },
        'free': { phonetic: '/friː/', meaning: '自由的；免费的；释放' },
        'frequent': { phonetic: '/ˈfriːkwənt/', meaning: '频繁的；时常发生的' },
        'full': { phonetic: '/fʊl/', meaning: '满的；充满的；完整的' },
        'general': { phonetic: '/ˈdʒenrəl/', meaning: '一般的；普通的；总的' },
        'good': { phonetic: '/ɡʊd/', meaning: '好的；良好的；好处' },
        'great': { phonetic: '/ɡreɪt/', meaning: '伟大的；重大的；极好的' },
        'grey': { phonetic: '/ɡreɪ/', meaning: '灰色的；阴沉的' },
        'hanging': { phonetic: '/ˈhæŋɪŋ/', meaning: '悬挂的；垂下的' },
        'happy': { phonetic: '/ˈhæpi/', meaning: '快乐的；幸福的' },
        'hard': { phonetic: '/hɑːd/', meaning: '硬的；困难的；努力的' },
        'healthy': { phonetic: '/ˈhelθi/', meaning: '健康的；有益于健康的' },
        'high': { phonetic: '/haɪ/', meaning: '高的；高级的；在高处' },
        'hollow': { phonetic: '/ˈhɒləʊ/', meaning: '空的；空心的；空洞的' },
        'important': { phonetic: '/ɪmˈpɔːtnt/', meaning: '重要的；重大的' },
        'kind': { phonetic: '/kaɪnd/', meaning: '和蔼的；友善的；种类' },
        'last': { phonetic: '/lɑːst/', meaning: '最后的；最近的；上一个' },
        'late': { phonetic: '/leɪt/', meaning: '迟的；晚的；已故的' },
        'living': { phonetic: '/ˈlɪvɪŋ/', meaning: '活着的；活的；生活' },
        'long': { phonetic: '/lɒŋ/', meaning: '长的；长久的；长期的' },
        'loose': { phonetic: '/luːs/', meaning: '松的；宽松的；松开' },
        'loud': { phonetic: '/laʊd/', meaning: '大声的；响亮的' },
        'low': { phonetic: '/ləʊ/', meaning: '低的；矮的；低下的' },
        'mixed': { phonetic: '/mɪkst/', meaning: '混合的；混杂的' },
        'narrow': { phonetic: '/ˈnærəʊ/', meaning: '狭窄的；窄小的' },
        'near': { phonetic: '/nɪə(r)/', meaning: '近的；接近的；在附近' },
        'necessary': { phonetic: '/ˈnesəsəri/', meaning: '必要的；必需的；必需品' },
        'new': { phonetic: '/njuː/', meaning: '新的；新鲜的；新出现的' },
        'normal': { phonetic: '/ˈnɔːml/', meaning: '正常的；平常的；标准的' },
        'old': { phonetic: '/əʊld/', meaning: '老的；旧的；古老的' },
        'open': { phonetic: '/ˈəʊpən/', meaning: '打开的；开放的；打开' },
        'opposite': { phonetic: '/ˈɒpəzɪt/', meaning: '对面的；相反的；对立物' },
        'parallel': { phonetic: '/ˈpærəlel/', meaning: '平行的；类似的' },
        'past': { phonetic: '/pɑːst/', meaning: '过去的；以前的；过去' },
        'physical': { phonetic: '/ˈfɪzɪkl/', meaning: '身体的；物质的；物理的' },
        'political': { phonetic: '/pəˈlɪtɪkl/', meaning: '政治的；与政治有关的' },
        'poor': { phonetic: '/pʊə(r)/', meaning: '贫穷的；可怜的；差的' },
        'possible': { phonetic: '/ˈpɒsəbl/', meaning: '可能的；可能发生的' },
        'present': { phonetic: '/ˈpreznt/', meaning: '现在的；出席的；礼物' },
        'private': { phonetic: '/ˈpraɪvət/', meaning: '私人的；私有的；秘密的' },
        'probable': { phonetic: '/ˈprɒbəbl/', meaning: '很可能的；大概的' },
        'quick': { phonetic: '/kwɪk/', meaning: '快的；迅速的；敏捷的' },
        'quiet': { phonetic: '/ˈkwaɪət/', meaning: '安静的；平静的；寂静' },
        'ready': { phonetic: '/ˈredi/', meaning: '准备好的；现成的；乐意的' },
        'red': { phonetic: '/red/', meaning: '红色的；红的' },
        'regular': { phonetic: '/ˈreɡjələ(r)/', meaning: '规则的；有规律的；常规的' },
        'responsible': { phonetic: '/rɪˈspɒnsəbl/', meaning: '有责任的；负责的' },
        'right': { phonetic: '/raɪt/', meaning: '正确的；右边的；权利' },
        'round': { phonetic: '/raʊnd/', meaning: '圆的；圆形的；在周围' },
        'rough': { phonetic: '/rʌf/', meaning: '粗糙的；不平的；艰难的' },
        'sad': { phonetic: '/sæd/', meaning: '伤心的；难过的；悲伤的' },
        'safe': { phonetic: '/seɪf/', meaning: '安全的；平安的；保险柜' },
        'same': { phonetic: '/seɪm/', meaning: '相同的；同样的；同样' },
        'second': { phonetic: '/ˈsekənd/', meaning: '第二的；次要的；秒' },
        'secret': { phonetic: '/ˈsiːkrət/', meaning: '秘密的；机密的；秘密' },
        'separate': { phonetic: '/ˈseprət/', meaning: '分开的；单独的；分离' },
        'serious': { phonetic: '/ˈsɪəriəs/', meaning: '严肃的；严重的；认真的' },
        'sharp': { phonetic: '/ʃɑːp/', meaning: '锋利的；尖的；敏锐的' },
        'short': { phonetic: '/ʃɔːt/', meaning: '短的；矮的；短暂的' },
        'simple': { phonetic: '/ˈsɪmpl/', meaning: '简单的；简易的；朴素的' },
        'slow': { phonetic: '/sləʊ/', meaning: '慢的；缓慢的；放慢' },
        'small': { phonetic: '/smɔːl/', meaning: '小的；少的；不重要的' },
        'smooth': { phonetic: '/smuːð/', meaning: '光滑的；平滑的；顺利的' },
        'soft': { phonetic: '/sɒft/', meaning: '柔软的；温柔的；软的' },
        'solid': { phonetic: '/ˈsɒlɪd/', meaning: '固体的；结实的；实心的' },
        'special': { phonetic: '/ˈspeʃl/', meaning: '特殊的；特别的；专门的' },
        'sticky': { phonetic: '/ˈstɪki/', meaning: '粘性的；胶粘的' },
        'straight': { phonetic: '/streɪt/', meaning: '直的；笔直的；直接' },
        'strong': { phonetic: '/strɒŋ/', meaning: '强壮的；强大的；强烈的' },
        'sudden': { phonetic: '/ˈsʌdn/', meaning: '突然的；忽然的' },
        'sweet': { phonetic: '/swiːt/', meaning: '甜的；甜蜜的；糖果' },
        'tall': { phonetic: '/tɔːl/', meaning: '高的；高大的' },
        'thick': { phonetic: '/θɪk/', meaning: '厚的；粗的；密的' },
        'thin': { phonetic: '/θɪn/', meaning: '薄的；细的；瘦的' },
        'tight': { phonetic: '/taɪt/', meaning: '紧的；绷紧的；紧身的' },
        'tired': { phonetic: '/ˈtaɪəd/', meaning: '疲倦的；疲劳的；累的' },
        'true': { phonetic: '/truː/', meaning: '真的；真实的；正确的' },
        'violent': { phonetic: '/ˈvaɪələnt/', meaning: '猛烈的；暴力的；激烈的' },
        'waiting': { phonetic: '/ˈweɪtɪŋ/', meaning: '等待的；等候的' },
        'warm': { phonetic: '/wɔːm/', meaning: '温暖的；暖和的；保暖' },
        'wet': { phonetic: '/wet/', meaning: '湿的；潮湿的；弄湿' },
        'white': { phonetic: '/waɪt/', meaning: '白色的；白的；白色' },
        'wide': { phonetic: '/waɪd/', meaning: '宽的；宽阔的；广泛的' },
        'wise': { phonetic: '/waɪz/', meaning: '明智的；聪明的；有智慧的' },
        'yellow': { phonetic: '/ˈjeləʊ/', meaning: '黄色的；黄的；黄色' },
        'young': { phonetic: '/jʌŋ/', meaning: '年轻的；幼小的；青年' }
    };

    // 导航高亮
    function setActive(el) {
        document.querySelectorAll('.grade-nav a').forEach(a => a.classList.remove('active'));
        el.classList.add('active');
    }
    // 滚动监听
    const sections = document.querySelectorAll('.grade-section');
    const navLinks = document.querySelectorAll('.grade-nav a');
    window.addEventListener('scroll', () => {
        let current = '';
        sections.forEach(section => {
            const sectionTop = section.offsetTop;
            if (scrollY >= sectionTop - 100) current = section.getAttribute('id');
        });
        navLinks.forEach(link => {
            link.classList.remove('active');
            if (link.getAttribute('href') === '#' + current) link.classList.add('active');
        });
    });
    // 复制链接
    function copyLink() {
        navigator.clipboard.writeText(window.location.href).then(() => {
            alert('链接已复制！');
        });
    }
    
    // 单词交互功能
    const wordInfo = document.getElementById('wordInfo');
    const infoWord = document.getElementById('infoWord');
    const infoPhonetic = document.getElementById('infoPhonetic');
    const infoMeaning = document.getElementById('infoMeaning');
    let hoverTimer;
    let currentWord = '';
    
    // 初始化所有单词元素
    function initWordElements() {
        const wordElements = document.querySelectorAll('.word-list li');
        wordElements.forEach(el => {
            const word = el.textContent.trim();
            el.addEventListener('click', () => {
                pronounceWord(word);
                showWordInfo(word, el);
            });
            el.addEventListener('mouseenter', () => {
                clearTimeout(hoverTimer);
                hoverTimer = setTimeout(() => {
                    showWordInfo(word, el);
                }, 800);
            });
            el.addEventListener('mouseleave', () => {
                clearTimeout(hoverTimer);
                hideWordInfo();
            });
        });
    }
    
    // 显示单词信息卡片
    function showWordInfo(word, element) {
        currentWord = word;
        const data = wordData[word];
        if (data) {
            infoWord.textContent = word;
            infoPhonetic.textContent = data.phonetic;
            infoMeaning.textContent = data.meaning;
        } else {
            infoWord.textContent = word;
            infoPhonetic.textContent = '';
            infoMeaning.textContent = '暂无翻译';
        }
    
        // 定位卡片
        const rect = element.getBoundingClientRect();
        let left = rect.right + 16;
        let top = rect.top;
    
        // 确保卡片不超出视窗
        if (left + 300 > window.innerWidth) {
            left = rect.left - 316;
        }
        if (top + 200 > window.innerHeight) {
            top = window.innerHeight - 200;
        }
        if (top < 0) {
            top = 16;
        }
    
        wordInfo.style.left = left + 'px';
        wordInfo.style.top = top + 'px';
        wordInfo.classList.add('show');
    }
    
    // 隐藏单词信息卡片
    function hideWordInfo() {
        wordInfo.classList.remove('show');
    }
    
    // 发音功能
    function pronounceWord(word) {
        if ('speechSynthesis' in window) {
            speechSynthesis.cancel(); // 取消之前的发音
            const utterance = new SpeechSynthesisUtterance(word);
            utterance.lang = 'en-US';
            utterance.rate = 0.9; // 稍微调整语速
            utterance.pitch = 1.1; // 调整音调
            utterance.volume = 1; // 音量
            
            // 尝试选择更好的语音
            const voices = speechSynthesis.getVoices();
            const preferredVoice = voices.find(v => 
                v.lang === 'en-US' && 
                (v.name.includes('Google') || v.name.includes('Natural') || v.name.includes('Female'))
            );
            if (preferredVoice) {
                utterance.voice = preferredVoice;
            }
            
            speechSynthesis.speak(utterance);
        }
    }
    
    // 点击其他地方隐藏卡片
    document.addEventListener('click', (e) => {
        if (!e.target.classList.contains('word-list') && !e.target.closest('.word-list')) {
            hideWordInfo();
        }
    });
    
    // 预加载语音列表
    if ('speechSynthesis' in window) {
        speechSynthesis.onvoiceschanged = () => {
            speechSynthesis.getVoices();
        };
    }
    
    // 初始化
    initWordElements();
</script>

</body>
</html>
