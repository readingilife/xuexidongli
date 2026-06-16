#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
import re
from pathlib import Path

BASE = Path(__file__).resolve().parent
DATA = BASE / "basic_english_850_data.json"
CHANGED_AUDIO = BASE / "changed_example_audio_paths.txt"

TEMPLATE_PREFIXES = (
    "Please use ",
    "We talked about ",
    "The word ",
    "This one is ",
)
TEMPLATE_SNIPPETS = (
    "matters to us.",
    "can happen at school.",
)

OPERATION_EXAMPLES = {
    "seem": ("You seem happy today.", "你今天看起来很开心。"),
    "be": ("Be kind to your friends.", "对朋友友善。"),
    "may": ("May I read this book?", "我可以读这本书吗？"),
    "will": ("I will try again.", "我会再试一次。"),
    "about": ("This story is about a family.", "这个故事是关于一个家庭的。"),
    "across": ("Walk across the bridge carefully.", "小心地走过桥。"),
    "after": ("Wash your hands after lunch.", "午饭后洗手。"),
    "against": ("Do not lean against the door.", "不要靠在门上。"),
    "among": ("The red ball is among the toys.", "红球在玩具中间。"),
    "at": ("Meet me at the gate.", "在大门口见我。"),
    "before": ("Brush your teeth before bed.", "睡前刷牙。"),
    "between": ("The pen is between two books.", "钢笔在两本书中间。"),
    "by": ("I sit by the window.", "我坐在窗边。"),
    "down": ("Please sit down.", "请坐下。"),
    "from": ("This letter is from my friend.", "这封信来自我的朋友。"),
    "in": ("The apple is in the bag.", "苹果在包里。"),
    "off": ("Take off your hat.", "摘下你的帽子。"),
    "on": ("The cup is on the table.", "杯子在桌子上。"),
    "over": ("The plane flies over the city.", "飞机飞过城市上空。"),
    "through": ("Light comes through the window.", "光从窗户照进来。"),
    "to": ("I go to school every day.", "我每天去上学。"),
    "under": ("The cat is under the chair.", "猫在椅子下面。"),
    "up": ("Stand up, please.", "请站起来。"),
    "with": ("I play with my sister.", "我和妹妹一起玩。"),
    "as": ("Use this box as a drum.", "把这个盒子当鼓用。"),
    "for": ("This gift is for you.", "这个礼物是给你的。"),
    "of": ("This is a cup of water.", "这是一杯水。"),
    "till": ("Wait till I come back.", "等到我回来。"),
    "than": ("My bag is bigger than yours.", "我的包比你的大。"),
    "a": ("I see a bird.", "我看见一只鸟。"),
    "the": ("The sun is bright.", "太阳很明亮。"),
    "all": ("All children can join the game.", "所有孩子都可以参加游戏。"),
    "any": ("Do you have any questions?", "你有任何问题吗？"),
    "every": ("Every child gets a turn.", "每个孩子都有一次机会。"),
    "no": ("There is no milk left.", "没有牛奶了。"),
    "other": ("Try the other door.", "试试另一扇门。"),
    "some": ("I need some paper.", "我需要一些纸。"),
    "such": ("Such a small seed can grow.", "这么小的种子也能生长。"),
    "that": ("That is my school.", "那是我的学校。"),
    "this": ("This is my pencil.", "这是我的铅笔。"),
    "I": ("I can read this word.", "我会读这个词。"),
    "he": ("He is my brother.", "他是我的兄弟。"),
    "you": ("You did a good job.", "你做得很好。"),
    "who": ("Who is at the door?", "谁在门口？"),
    "and": ("I like apples and bananas.", "我喜欢苹果和香蕉。"),
    "because": ("I smile because I am happy.", "我笑是因为我开心。"),
    "but": ("It is cold, but I am warm.", "天气冷，但我很暖和。"),
    "or": ("Do you want milk or water?", "你想要牛奶还是水？"),
    "if": ("If it rains, take an umbrella.", "如果下雨，就带伞。"),
    "though": ("Though it is hard, I can try.", "虽然很难，我也能试试。"),
    "while": ("Read a book while you wait.", "等待的时候读本书。"),
    "how": ("How do you spell your name?", "你的名字怎么拼？"),
    "when": ("When is your birthday?", "你的生日是什么时候？"),
    "where": ("Where is my bag?", "我的包在哪里？"),
    "why": ("Why is the sky blue?", "天空为什么是蓝色的？"),
    "again": ("Please say it again.", "请再说一遍。"),
    "ever": ("Have you ever seen snow?", "你见过雪吗？"),
    "far": ("My home is not far.", "我家不远。"),
    "forward": ("Take one step forward.", "向前走一步。"),
    "here": ("Come here, please.", "请到这里来。"),
    "near": ("The school is near my home.", "学校离我家很近。"),
    "now": ("Now it is your turn.", "现在轮到你了。"),
    "out": ("Go out and play.", "出去玩吧。"),
    "still": ("I still remember the song.", "我仍然记得那首歌。"),
    "then": ("Finish your work, then play.", "先完成作业，然后再玩。"),
    "there": ("There is a book on the desk.", "桌上有一本书。"),
    "together": ("We read together.", "我们一起读书。"),
    "well": ("You read very well.", "你读得很好。"),
    "almost": ("I almost finished the puzzle.", "我差点完成了拼图。"),
    "enough": ("I have enough pencils.", "我有足够的铅笔。"),
    "even": ("Even a small step helps.", "哪怕一小步也有帮助。"),
    "little": ("A little bird is in the tree.", "一只小鸟在树上。"),
    "much": ("Thank you very much.", "非常感谢你。"),
    "not": ("Do not run in the hall.", "不要在走廊里跑。"),
    "only": ("I have only one ticket.", "我只有一张票。"),
    "quite": ("The room is quite quiet.", "房间相当安静。"),
    "so": ("The cake is so sweet.", "蛋糕太甜了。"),
    "very": ("This book is very funny.", "这本书很有趣。"),
    "tomorrow": ("We will visit grandma tomorrow.", "我们明天去看奶奶。"),
    "yesterday": ("I saw a rainbow yesterday.", "我昨天看见了彩虹。"),
    "north": ("The library is north of the park.", "图书馆在公园北边。"),
    "south": ("The river is south of our school.", "河在我们学校南边。"),
    "east": ("The sun rises in the east.", "太阳从东方升起。"),
    "west": ("The sun sets in the west.", "太阳从西方落下。"),
    "please": ("Please open the door.", "请打开门。"),
    "yes": ("Yes, I can help.", "是的，我可以帮忙。"),
}

SPECIAL_EXAMPLES = {
    "account": ("I keep an account of my stickers.", "我记录自己的贴纸数量。"),
    "act": ("The actor can act on stage.", "演员可以在舞台上表演。"),
    "addition": ("Addition helps us count more.", "加法帮助我们数得更多。"),
    "advertisement": ("An advertisement shows a new toy.", "广告展示一个新玩具。"),
    "air": ("Fresh air comes through the window.", "新鲜空气从窗户进来。"),
    "animal": ("A dog is an animal.", "狗是一种动物。"),
    "answer": ("Write the answer on the line.", "把答案写在线上。"),
    "argument": ("Stop the argument and listen.", "停止争论，先听一听。"),
    "art": ("We make art with color.", "我们用颜色做艺术作品。"),
    "attack": ("Do not attack other people.", "不要攻击别人。"),
    "authority": ("A teacher has authority in class.", "老师在课堂上有管理权。"),
    "behavior": ("Good behavior keeps class calm.", "好的行为让课堂安静。"),
    "bite": ("Do not bite your pencil.", "不要咬铅笔。"),
    "blood": ("Blood moves inside our bodies.", "血液在我们身体里流动。"),
    "body": ("Move your body when you exercise.", "运动时活动你的身体。"),
    "bread": ("I eat bread for breakfast.", "我早餐吃面包。"),
    "breath": ("Take a deep breath.", "深呼吸一下。"),
    "brother": ("My brother plays with me.", "我的兄弟和我一起玩。"),
    "building": ("The building is near our school.", "这栋建筑在我们学校附近。"),
    "burn": ("Do not touch a burn.", "不要碰烧伤的地方。"),
    "business": ("A shop is a small business.", "商店是一种小生意。"),
    "butter": ("Put butter on the bread.", "把黄油抹在面包上。"),
    "care": ("Take care of your books.", "爱护你的书。"),
    "chalk": ("The teacher writes with chalk.", "老师用粉笔写字。"),
    "chance": ("Everyone gets a chance to speak.", "每个人都有机会发言。"),
    "color": ("What color is your bag?", "你的包是什么颜色？"),
    "condition": ("Rain is a bad condition for a picnic.", "下雨不适合野餐。"),
    "connection": ("This line shows a connection.", "这条线表示连接。"),
    "control": ("Control your voice in the library.", "在图书馆控制音量。"),
    "country": ("China is a big country.", "中国是一个大国家。"),
    "crime": ("A crime breaks the law.", "犯罪是违反法律的事。"),
    "crush": ("Do not crush the paper cup.", "不要压扁纸杯。"),
    "cry": ("The baby may cry when hungry.", "宝宝饿了可能会哭。"),
    "danger": ("Stay away from danger.", "远离危险。"),
    "death": ("Death means a life has ended.", "死亡表示生命结束了。"),
    "decision": ("Make a good decision.", "做一个好的决定。"),
    "disease": ("Wash hands to stop disease.", "洗手可以预防疾病。"),
    "drink": ("I drink water after class.", "下课后我喝水。"),
    "education": ("Education helps children grow.", "教育帮助孩子成长。"),
    "example": ("This is a good example.", "这是一个好例子。"),
    "family": ("My family eats dinner together.", "我的家人一起吃晚饭。"),
    "father": ("My father reads with me.", "爸爸陪我读书。"),
    "fight": ("We should not fight at school.", "我们不应该在学校打架。"),
    "friend": ("A good friend shares toys.", "好朋友会分享玩具。"),
    "government": ("The government makes rules for a city.", "政府为城市制定规则。"),
    "history": ("History tells stories from the past.", "历史讲过去的故事。"),
    "knowledge": ("Reading gives us knowledge.", "阅读给我们知识。"),
    "kick": ("Kick the ball into the goal.", "把球踢进球门。"),
    "kiss": ("Give grandma a kiss on the cheek.", "亲亲奶奶的脸颊。"),
    "language": ("English is a language.", "英语是一种语言。"),
    "law": ("A law is an important rule.", "法律是重要的规则。"),
    "learning": ("Learning a word takes practice.", "学会一个词需要练习。"),
    "love": ("I love my family.", "我爱我的家人。"),
    "money": ("Save your money in a box.", "把钱存在盒子里。"),
    "mother": ("My mother smiles at me.", "妈妈对我微笑。"),
    "milk": ("I drink milk at breakfast.", "我早餐喝牛奶。"),
    "music": ("Music makes me happy.", "音乐让我开心。"),
    "news": ("The news tells what happened.", "新闻告诉我们发生了什么。"),
    "pain": ("Tell an adult if you feel pain.", "如果疼，要告诉大人。"),
    "peace": ("Peace means no fighting.", "和平表示没有打斗。"),
    "person": ("Every person has a name.", "每个人都有名字。"),
    "poison": ("Do not touch poison.", "不要碰有毒物。"),
    "prison": ("A prison keeps dangerous people away.", "监狱让危险的人远离大家。"),
    "punishment": ("A fair punishment teaches a lesson.", "公平的惩罚是为了让人学会。"),
    "question": ("Ask a question if you do not know.", "不知道就提问。"),
    "religion": ("Religion is important to many families.", "宗教对许多家庭很重要。"),
    "respect": ("Show respect when others speak.", "别人说话时要表示尊重。"),
    "reward": ("A sticker is a small reward.", "贴纸是一个小奖励。"),
    "sex": ("Ask a parent about the word sex.", "关于 sex 这个词，请问家长。"),
    "smash": ("Do not smash the toy.", "不要砸坏玩具。"),
    "society": ("People live together in society.", "人们在社会中一起生活。"),
    "story": ("Tell me a short story.", "给我讲一个短故事。"),
    "support": ("Friends support each other.", "朋友互相支持。"),
    "system": ("A school has a system of rules.", "学校有一套规则系统。"),
    "tax": ("Adults pay tax to help the city.", "大人缴税来帮助城市运转。"),
    "theory": ("A theory is an idea to explain things.", "理论是用来解释事情的想法。"),
    "trouble": ("Ask for help when you are in trouble.", "遇到麻烦时请求帮助。"),
    "war": ("War hurts many families.", "战争会伤害许多家庭。"),
    "water": ("Drink water after running.", "跑步后喝水。"),
    "wine": ("Wine is a drink for adults.", "葡萄酒是成人饮品。"),
    "work": ("Finish your work before play.", "玩之前先完成任务。"),
}

SPECIAL_EXAMPLES.update({
    "attempt": ("I will attempt the puzzle.", "我会尝试这个拼图。"),
    "blow": ("Blow the balloon gently.", "轻轻吹气球。"),
    "burst": ("The balloon may burst.", "气球可能会爆开。"),
    "change": ("I can change my answer.", "我可以修改答案。"),
    "cough": ("Cover your mouth when you cough.", "咳嗽时捂住嘴。"),
    "cover": ("Cover the box with paper.", "用纸盖住盒子。"),
    "damage": ("Do not damage the book.", "不要损坏这本书。"),
    "digestion": ("Digestion turns food into energy.", "消化把食物变成能量。"),
    "driving": ("Driving a car is for adults.", "开车是大人的事。"),
    "exchange": ("We exchange cards after class.", "下课后我们交换卡片。"),
    "fall": ("Do not fall on the wet floor.", "不要在湿地板上摔倒。"),
    "feeling": ("A happy feeling makes me smile.", "开心的感觉让我微笑。"),
    "flight": ("The bird is in flight.", "鸟正在飞行。"),
    "fold": ("Fold the paper in half.", "把纸对折。"),
    "grip": ("Grip the pencil gently.", "轻轻握住铅笔。"),
    "hearing": ("Good hearing helps us listen.", "好的听力帮助我们倾听。"),
    "help": ("I can help my friend.", "我可以帮助朋友。"),
    "join": ("Join the game with us.", "加入我们的游戏。"),
    "jump": ("Jump over the line.", "跳过这条线。"),
    "laugh": ("The funny story made me laugh.", "有趣的故事让我笑。"),
    "lead": ("Lead the line to the door.", "带队走到门口。"),
    "lift": ("Lift the box with two hands.", "用两只手抬盒子。"),
    "look": ("Look at the picture.", "看这张图片。"),
    "move": ("Move your chair quietly.", "轻轻移动你的椅子。"),
    "play": ("Play a game after homework.", "作业后玩一个游戏。"),
    "polish": ("Polish your shoes with a cloth.", "用布擦亮鞋子。"),
    "protest": ("People protest when rules are unfair.", "规则不公平时，人们会抗议。"),
    "pull": ("Pull the door open.", "把门拉开。"),
    "push": ("Push the chair under the desk.", "把椅子推进桌子下面。"),
    "reading": ("Reading helps me learn.", "阅读帮助我学习。"),
    "roll": ("Roll the ball to me.", "把球滚给我。"),
    "rub": ("Rub your hands together.", "搓搓你的双手。"),
    "run": ("Run on the playground.", "在操场上跑步。"),
    "shake": ("Shake the bottle gently.", "轻轻摇瓶子。"),
    "sleep": ("Sleep early tonight.", "今晚早点睡。"),
    "slip": ("Do not slip on the wet floor.", "不要在湿地板上滑倒。"),
    "smell": ("Smell the flower.", "闻一闻花。"),
    "smile": ("Smile at your friend.", "对朋友微笑。"),
    "sneeze": ("Cover your nose when you sneeze.", "打喷嚏时捂住鼻子。"),
    "sound": ("The bell makes a loud sound.", "铃发出很大的声音。"),
    "start": ("Start your work now.", "现在开始做事。"),
    "stitch": ("A stitch holds the cloth together.", "针脚把布连在一起。"),
    "stop": ("Stop at the red light.", "红灯时停下。"),
    "stretch": ("Stretch your arms after sitting.", "坐久后伸展手臂。"),
    "swim": ("Swim with an adult nearby.", "游泳时要有大人在旁边。"),
    "talk": ("Talk softly in the library.", "在图书馆轻声说话。"),
    "taste": ("Taste the soup carefully.", "小心尝一尝汤。"),
    "teaching": ("Teaching helps others learn.", "教学帮助别人学习。"),
    "touch": ("Do not touch the hot cup.", "不要碰热杯子。"),
    "transport": ("A bus can transport students.", "公交车可以运送学生。"),
    "turn": ("Turn the page slowly.", "慢慢翻页。"),
    "twist": ("Twist the cap to open it.", "拧瓶盖把它打开。"),
    "use": ("Use a pencil to write.", "用铅笔写字。"),
    "view": ("The window has a nice view.", "窗外有好看的景色。"),
    "voice": ("Use a quiet voice indoors.", "在室内用轻声。"),
    "walk": ("Walk slowly in the hall.", "在走廊里慢慢走。"),
    "wash": ("Wash your hands before eating.", "吃饭前洗手。"),
    "writing": ("Writing helps me remember words.", "写字帮助我记住单词。"),
})

QUALITY_EXAMPLES = {
    "able": ("I am able to read this page.", "我能读这一页。"),
    "acid": ("A lemon can taste acid.", "柠檬可能尝起来酸。"),
    "angry": ("I feel angry, so I take a breath.", "我生气了，所以深呼吸。"),
    "automatic": ("The door is automatic.", "这扇门是自动的。"),
    "black": ("The cat is black.", "这只猫是黑色的。"),
    "boiling": ("The water is boiling.", "水正在沸腾。"),
    "broken": ("The toy is broken.", "玩具坏了。"),
    "cheap": ("This pencil is cheap.", "这支铅笔很便宜。"),
    "chemical": ("A chemical can be dangerous.", "化学物质可能有危险。"),
    "chief": ("The chief reason is safety.", "最主要的原因是安全。"),
    "clean": ("My hands are clean.", "我的手很干净。"),
    "clear": ("The sky is clear today.", "今天的天空很晴朗。"),
    "cold": ("The milk is cold.", "牛奶是冷的。"),
    "common": ("Common words are useful.", "常见词很有用。"),
    "complete": ("My homework is complete.", "我的作业完成了。"),
    "complex": ("This puzzle is complex.", "这个拼图很复杂。"),
    "cruel": ("A cruel joke can hurt someone.", "残忍的玩笑会伤害别人。"),
    "deep": ("The water is deep.", "水很深。"),
    "early": ("I get up early.", "我起得很早。"),
    "electric": ("This is an electric fan.", "这是一台电风扇。"),
    "equal": ("Two plus two is equal to four.", "二加二等于四。"),
    "fertile": ("Fertile soil helps plants grow.", "肥沃的土壤帮助植物生长。"),
    "first": ("This is my first try.", "这是我的第一次尝试。"),
    "flat": ("The table is flat.", "桌面是平的。"),
    "free": ("The bird is free.", "鸟儿是自由的。"),
    "frequent": ("Frequent practice helps memory.", "经常练习帮助记忆。"),
    "full": ("My cup is full.", "我的杯子满了。"),
    "general": ("This is a general rule.", "这是一条一般规则。"),
    "hard": ("This rock is hard.", "这块石头很硬。"),
    "healthy": ("Healthy food helps us grow.", "健康的食物帮助我们成长。"),
    "hollow": ("This box is hollow.", "这个盒子是空心的。"),
    "kind": ("Be kind to younger children.", "对年幼的孩子友善。"),
    "like": ("I like this picture.", "我喜欢这张图片。"),
    "male": ("A boy is male.", "男孩是男性。"),
    "married": ("My parents are married.", "我的父母结婚了。"),
    "material": ("Cotton is a soft material.", "棉花是一种柔软的材料。"),
    "medical": ("A medical mask keeps us safe.", "医用口罩保护我们。"),
    "military": ("A military parade has soldiers.", "军事游行中有士兵。"),
    "natural": ("Natural light comes from the sun.", "自然光来自太阳。"),
    "necessary": ("Rest is necessary for children.", "休息对孩子是必要的。"),
    "new": ("This is my new book.", "这是我的新书。"),
    "normal": ("It is a normal school day.", "这是普通的上学日。"),
    "open": ("The door is open.", "门开着。"),
    "parallel": ("These two lines are parallel.", "这两条线是平行的。"),
    "past": ("Past days are behind us.", "过去的日子已经在身后。"),
    "probable": ("Rain is probable today.", "今天很可能下雨。"),
    "political": ("Political news is for adults.", "政治新闻主要给大人看。"),
    "present": ("Stay in the present moment.", "专心在现在这一刻。"),
    "private": ("This diary is private.", "这本日记是私人的。"),
    "public": ("The park is public.", "公园是公共的。"),
    "quick": ("The rabbit is quick.", "兔子跑得快。"),
    "quiet": ("The room is quiet.", "房间很安静。"),
    "ready": ("I am ready for class.", "我准备好上课了。"),
    "responsible": ("A responsible child keeps promises.", "有责任心的孩子会守诺言。"),
    "round": ("The moon is round.", "月亮是圆的。"),
    "same": ("The two colors are the same.", "这两个颜色相同。"),
    "second": ("This is my second try.", "这是我的第二次尝试。"),
    "separate": ("Keep clean socks separate.", "把干净袜子分开放。"),
    "serious": ("This is a serious problem.", "这是个严肃的问题。"),
    "sharp": ("A knife is sharp.", "刀很锋利。"),
    "smooth": ("The stone is smooth.", "石头很光滑。"),
    "straight": ("Draw a straight line.", "画一条直线。"),
    "strong": ("My legs are strong.", "我的腿很有力。"),
    "violent": ("A violent game can scare children.", "暴力游戏可能吓到孩子。"),
    "future": ("This is my future plan.", "这是我未来的计划。"),
    "last": ("This is the last page.", "这是最后一页。"),
    "late": ("The bus is late.", "公交车晚点了。"),
    "left": ("Use your left hand.", "用你的左手。"),
    "opposite": ("The doors are on opposite sides.", "门在相对的两边。"),
}

FORCE_REFRESH = {
    "act", "attack", "bite", "body", "building", "burn", "common", "crush",
    "drink", "fight", "kick", "kiss", "like", "material", "milk", "past",
    "present", "smash", "chief", "first", "frequent", "future", "general",
    "last", "late", "left", "natural", "necessary", "new", "normal",
    "opposite", "probable", "same", "second",
}


def is_template(sentence):
    return (
        sentence.startswith(TEMPLATE_PREFIXES)
        or any(snippet in sentence for snippet in TEMPLATE_SNIPPETS)
        or (sentence.startswith("We can ") and sentence.endswith(" safely."))
    )


def article(word):
    return "an" if word[:1].lower() in "aeiou" else "a"


def fallback_example(item):
    word = item["word"]
    category = item.get("category")
    child_meaning = item.get("childMeaning") or word
    if word in OPERATION_EXAMPLES:
        return OPERATION_EXAMPLES[word]
    if word in SPECIAL_EXAMPLES:
        return SPECIAL_EXAMPLES[word]
    if word in QUALITY_EXAMPLES:
        return QUALITY_EXAMPLES[word]
    if category == "Things — Picturable":
        return (f"Look at the {word}.", f"看这个{child_meaning}。")
    if category == "Qualities":
        return quality_fallback(word, child_meaning)
    if category == "Operations":
        return (f"Can you use {word} here?", f"你能在这里用 {word} 吗？")
    if category == "Things — General":
        return general_fallback(word, child_meaning, item.get("difficulty"))
    return (f"I can learn the word {word}.", f"我能学习 {word} 这个词。")


def general_fallback(word, child_meaning, difficulty):
    visible = {
        "back", "body", "brass", "canvas", "cloth", "coal", "copper", "cork",
        "cotton", "crack", "curve", "dust", "earth", "edge", "field", "fire",
        "flame", "food", "front", "fruit", "glass", "gold", "grain", "grass",
        "hole", "ice", "ink", "insect", "instrument", "iron", "jelly", "land",
        "leather", "letter", "linen", "liquid", "machine", "mark", "meal",
        "meat", "metal", "milk", "mist", "mountain", "night", "oil", "page",
        "paint", "paper", "paste", "place", "plant", "powder", "rain", "ray",
        "river", "road", "room", "salt", "sand", "scale", "sea", "seat",
        "shade", "side", "sign", "silk", "silver", "sky", "smoke", "snow",
        "soap", "soup", "space", "steam", "steel", "step", "stone", "sugar",
        "summer", "thunder", "tin", "top", "vessel", "water", "wave", "wax",
        "weather", "wind", "winter", "wood", "wool",
    }
    people = {
        "cook", "daughter", "expert", "guide", "judge", "manager", "man",
        "owner", "porter", "representative", "secretary", "servant", "sister",
        "son", "woman",
    }
    actions = {
        "act", "attack", "attempt", "bite", "blow", "burn", "burst", "change",
        "cough", "cover", "crush", "damage", "digestion", "drink", "driving",
        "exchange", "fall", "feeling", "fight", "flight", "fold", "grip",
        "hearing", "help", "join", "jump", "kick", "kiss", "laugh", "lead",
        "lift", "look", "move", "play", "polish", "protest", "pull", "push",
        "reading", "roll", "rub", "run", "shake", "sleep", "slip", "smash",
        "smell", "smile", "sneeze", "sound", "start", "stitch", "stop",
        "stretch", "swim", "talk", "taste", "teaching", "touch", "transport",
        "turn", "twist", "use", "view", "voice", "walk", "wash", "writing",
    }
    school_words = {
        "adjustment", "amount", "approval", "attention", "base", "belief",
        "bit", "cause", "comfort", "committee", "company", "comparison",
        "competition", "credit", "current", "debt", "degree", "design",
        "detail", "development", "direction", "discovery", "discussion",
        "distance", "division", "doubt", "effect", "end", "error", "event",
        "experience", "fact", "fear", "fiction", "force", "form", "group",
        "growth", "harmony", "hate", "heat", "hope", "hour", "humor", "idea",
        "impulse", "increase", "industry", "insurance", "interest",
        "invention", "journey", "level", "limit", "list", "loss", "market",
        "mass", "measure", "meeting", "memory", "middle", "mind", "minute",
        "motion", "name", "nation", "need", "noise", "note", "number",
        "observation", "offer", "operation", "opinion", "order",
        "organization", "part", "payment", "pleasure", "point", "position",
        "power", "price", "process", "profit", "property", "purpose",
        "quality", "range", "rate", "reaction", "reason", "record", "regret",
        "relation", "request", "rest", "rhythm", "rule", "science",
        "selection", "self", "sense", "size", "sort", "stage", "statement",
        "structure", "substance", "suggestion", "system", "tendency", "test",
        "time", "trick", "value", "way", "week", "weight", "word", "year",
    }
    if word in visible:
        return (f"I can see the {word}.", f"我能看见这个{child_meaning}。")
    if word in people:
        return (f"The {word} helped us today.", f"这个{child_meaning}今天帮助了我们。")
    if word in actions:
        return (f"We can {word} safely.", f"我们可以安全地{child_meaning}。")
    if word in school_words:
        return (f"A clear example helps me understand {word}.", f"一个清楚的例子帮助我理解{child_meaning}。")
    if difficulty == "extension":
        return (f"Ask an adult to explain {word}.", f"请大人解释 {word}。")
    return (f"I can learn {word} with an example.", f"我可以通过例子学习{child_meaning}。")


def quality_fallback(word, child_meaning):
    noun_by_word = {
        "beautiful": "flower", "bright": "lamp", "brown": "bear", "chief": "idea",
        "common": "word", "conscious": "person", "cut": "paper",
        "dependent": "baby", "elastic": "band", "fat": "cat", "first": "page",
        "fixed": "seat", "frequent": "practice", "general": "rule",
        "great": "day", "grey": "cloud", "hanging": "coat", "high": "wall",
        "important": "rule", "like": "picture", "living": "plant", "long": "road",
        "material": "bag", "mixed": "colors", "natural": "light",
        "necessary": "rest", "new": "book", "normal": "day", "past": "week",
        "physical": "game", "poor": "family", "possible": "answer",
        "present": "moment", "probable": "answer", "regular": "practice",
        "right": "answer", "same": "color", "second": "try", "sticky": "glue",
        "stiff": "card", "sudden": "sound", "sweet": "apple", "tall": "tree",
        "thick": "book", "tight": "shoe", "tired": "child", "true": "story",
        "waiting": "child", "warm": "coat", "wet": "towel", "wide": "road",
        "wise": "choice", "yellow": "banana", "young": "child", "awake": "baby",
        "bent": "spoon", "bitter": "tea", "certain": "answer",
        "comfortable": "chair", "dark": "room", "dead": "leaf", "dear": "friend",
        "delicate": "cup", "different": "shapes", "dirty": "shoe", "dry": "shirt",
        "false": "answer", "feeble": "voice", "female": "teacher",
        "foolish": "choice", "future": "plan", "green": "leaf", "ill": "child",
        "last": "page", "late": "bus", "left": "hand", "loose": "button",
        "loud": "bell", "low": "table", "narrow": "path", "old": "house",
        "opposite": "side", "rough": "stone", "safe": "place", "secret": "note",
        "short": "story", "shut": "door", "simple": "question", "slow": "train",
        "soft": "pillow", "solid": "wall", "special": "gift",
        "strange": "sound", "thin": "paper", "white": "cloud", "wrong": "answer",
    }
    noun = noun_by_word.get(word, "thing")
    plural = noun.endswith("s")
    be = "are" if plural else "is"
    article_text = f"The {noun}" if plural else f"The {noun}"
    return (f"{article_text} {be} {word}.", f"这个例句表示：{child_meaning}。")


def update_example_question(item):
    examples = item.get("examples") or []
    if not examples:
        return
    sentence = examples[0].get("en", "")
    word = item["word"]
    if word.lower() in sentence.lower():
        pattern = rf"\b{re.escape(word)}\b"
        if not re.search(pattern, sentence, flags=re.I):
            return
        item["exampleQuestion"] = {
            "sentence": re.sub(pattern, "___", sentence, count=1, flags=re.I),
            "answer": word,
        }


def main():
    words = json.loads(DATA.read_text(encoding="utf-8"))
    changed_audio_paths = []
    changed_count = 0

    for item in words:
        replacement = None
        for example in item.get("examples") or []:
            needs_cn_fix = "的的" in example.get("cn", "")
            if (
                not is_template(example.get("en", ""))
                and item["word"] not in FORCE_REFRESH
                and not needs_cn_fix
            ):
                continue
            if replacement is None:
                replacement = fallback_example(item)
            new_en, new_cn = replacement
            if example.get("en") != new_en:
                changed_count += 1
                if example.get("audio"):
                    changed_audio_paths.append(example["audio"])
            example["en"] = new_en
            example["cn"] = new_cn
        update_example_question(item)

    DATA.write_text(json.dumps(words, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    CHANGED_AUDIO.write_text("\n".join(sorted(set(changed_audio_paths))) + "\n", encoding="utf-8")
    print(f"replaced template examples: {changed_count}")
    print(f"changed audio paths: {len(set(changed_audio_paths))}")
    print(f"wrote {CHANGED_AUDIO}")


if __name__ == "__main__":
    main()
