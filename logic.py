import pandas as pd
import re

Department = {
"英文学科 English Linguistic and Education" : {
"English skills Ⅰ" : ([
"Reading Literature in EnglishⅠ",
"Reading Literature in EnglishⅡ",
"English PhoneticsⅠ",
"English PhoneticsⅡ",
"Basic Reading & WritingⅠ",
"Basic Reading & WritingⅡ",
"Listening & SpeakingⅠ",
"Listening & SpeakingⅡ",
"Discussion & Debate",
"Advanced Reading & Writing "
], 20),
"English skills Ⅱ" : ([
"English GrammarⅠ",
"English GrammarⅡ",
"Media EnglishⅠ (TV News)",
"Media EnglishⅡ (Magazines)",
"SpeechⅠ",
"SpeechⅡ",
"Advanced Discussion & Debate",
"Presentation ",
"TOEIC WorkshopⅠ",
"TOEIC WorkshopⅡ",
"TOEFL Workshop",
"English through Drama",
"Current Issues in ESWⅠ",
"Current Issues in ESWⅡ",
"Business EnglishⅠ",
"Business EnglishⅡ",
"Hospitality EnglishⅠ",
"Hospitality EnglishⅡ",
"Translation"
], 8),
"World Englishes and Literature" : ([
"World EnglishesⅠ",
"World EnglishesⅡ",
"World LiteratureⅠ",
"World LiteratureⅡ",
"Japanese Literature in English",
"Classic Literature",
"Introducing Mt. FujiⅠ",
"Introducing Mt. FujiⅡ",
"Introducing JapanⅠ",
"Introducing JapanⅡ",
"Comparative CultureⅠ",
"Comparative CultureⅡ",
"Intercultural CommunicationⅠ",
"Intercultural CommunicationⅡ",
"Asian Literature in English",
"Children's Literature""Gender and SexualityⅠ",
"Gender and SexualityⅡ",
"Transnational LiteratureⅠ",
"Transnational LiteratureⅡ",
"Ethnic Minority LiteratureⅠ",
"Ethnic Minority LiteratureⅡ",
"Japonism",
"Cultural Studies",
], 10),
"English Linguistics and Education" : ([
"Introduction to English LinguisticsⅠ",
"Introduction to English LinguisticsⅡ",
"Communication StudiesⅠ",
"Communication StudiesⅡ",
"Language and CultureⅠ",
"Language and CultureⅡ",
"Introduction to SLA and ELTⅠ",
"Introduction to SLA and ELTⅡ",
"Topics in LinguisticsⅠ",
"Topics in LinguisticsⅡ",
"Applied LinguisticsⅠ",
"Applied LinguisticsⅡ",
"First Language Acquisition",
"Second Language Acquisition",
"SociolinguisticsⅠ",
"SociolinguisticsⅡ",
"Issues in TESOLⅠ",
"Issues in TESOLⅡ",
"TEFL（英語科教育法）Ⅰ",
"TEFL（英語科教育法）Ⅱ",
"TEFL（英語科教育法）Ⅲ",
"TEFL（英語科教育法）Ⅳ",
"Elementary School English Education",
"TEFL in PracticeⅠ",
"TEFL in PracticeⅡ",
], 20),
"Seminar" : ([
"Seminar in Language and CultureⅠ",
"Seminar in Language and CultureⅡ",
"Seminar in Language and CultureⅢ",
"Seminar in Language and CultureⅣ",
], 8),
"卒業論文" : ([
"卒業論文"
], 4),
"外国語科目" : ([
"English Foundations Ⅰ",
"English Foundations Ⅱ",
"English TELL Ⅰ",
"English TELL Ⅱ",
"EAP 1 (Academic Listening, Discussion & Presentation) Ⅰ",
"EAP 1 (Academic Listening, Discussion & Presentation) Ⅱ",
"EAP 2 (Academic Reading & Writing) Ⅰ",
"EAP 2 (Academic Reading & Writing) Ⅱ",
"Advanced English TELL Ⅰ",
"Advanced English TELL Ⅱ",
"Extensive Reading",
"Intensive Reading",
"Movie English Ⅰ",
"Movie English Ⅱ",
"English for Business Ⅰ",
"English for Business Ⅱ",
"ドイツ語総合Ⅰ",
"ドイツ語総合Ⅱ",
"ドイツ語演習Ⅰ",
"ドイツ語演習Ⅱ",
"German Intermediate (B1) Ⅰ",
"German Intermediate (B1) Ⅱ",
"フランス語総合Ⅰ",
"フランス語総合Ⅱ",
"フランス語演習Ⅰ",
"フランス語演習Ⅱ",
"French Intermediate (B1) Ⅰ",
"French Intermediate (B1) Ⅱ",
"中国語総合Ⅰ",
"中国語総合Ⅱ",
"中国語演習Ⅰ",
"中国語演習Ⅱ",
"中国語応用演習Ⅰ",
"中国語応用演習Ⅱ",
"韓国朝鮮語総合Ⅰ",
"韓国朝鮮語総合Ⅱ",
"韓国朝鮮語演習Ⅰ",
"韓国朝鮮語演習Ⅱ",
"韓国朝鮮語応用演習Ⅰ",
"韓国朝鮮語応用演習Ⅱ",
"スペイン語総合Ⅰ",
"スペイン語総合Ⅱ",
"スペイン語演習Ⅰ",
"スペイン語演習Ⅱ",
"Spanish Intermediate (B1) Ⅰ",
"Spanish Intermediate (B1) Ⅱ",
"日本語アカデミック・プレゼンテーションⅠ",
"日本語アカデミック・プレゼンテーションⅡ",
"日本語アカデミック・ライティングⅠ",
"日本語アカデミック・ライティングⅡ",
"日本語読解Ⅰ",
"日本語読解Ⅱ",
"日本語能力総合演習Ⅰ",
"日本語能力総合演習Ⅱ",
"日本語総合研究活動Ⅰ",
"日本語総合研究活動Ⅱ",
"就職・仕事の日本語Ⅰ",
"就職・仕事の日本語Ⅱ",
"日本語待遇表現Ⅰ",
"日本語待遇表現Ⅱ"
], 8),
"教養科目" : ([
"アカデミック・スキルズ",
"自然と生命Ⅰ",
"自然と生命Ⅱ",
"自然と生命Ⅲ",
"自然と生命Ⅳ",
"自然と生命Ⅴ",
"自然と生命Ⅵ",
"自然と生命Ⅶ",
"世界と自己Ⅰ",
"世界と自己Ⅱ",
"世界と自己Ⅲ",
"世界と自己Ⅳ",
"世界と自己Ⅴ",
"世界と自己Ⅵ",
"世界と自己Ⅶ",
"世界と自己Ⅷ",
"世界と自己Ⅸ",
"世界と自己Ⅹ",
"日本国憲法",
"市民と社会Ⅰ",
"市民と社会Ⅱ",
"市民と社会Ⅲ",
"市民と社会Ⅳ",
"市民と社会Ⅴ",
"市民と社会Ⅵ",
"歴史と文化Ⅰ",
"歴史と文化Ⅱ",
"歴史と文化Ⅲ",
"歴史と文化Ⅳ",
"歴史と文化Ⅴ",
"歴史と文化Ⅵ",
"歴史と文化Ⅶ",
"歴史と文化Ⅷ",
"歴史と文化Ⅸ",
"現代の課題Ⅰ",
"現代の課題Ⅱ",
"現代の課題Ⅲ",
"現代の課題Ⅳ",
"現代の課題Ⅴ",
"現代の課題Ⅵ",
"現代の課題Ⅶ",
"現代の課題Ⅷ",
"デジタルシティズンシップ入門",
"データサイエンス（プログラミング）",
"データサイエンス（リテラシー）",
"データサイエンス（応用）",
"データサイエンス演習Ⅰ",
"データサイエンス演習Ⅱ",
"ジェンダー研究入門",
"ジェンダー研究への誘い",
"ジェンダー研究Ⅰ",
"ジェンダー研究Ⅱ",
"ジェンダー研究Ⅲ",
"ジェンダー研究Ⅳ",
"ジェンダー研究Ⅴ",
"ジェンダー研究Ⅵ",
"フィールド・ミュージアム入門",
"フィールド・ミュージアム研究Ⅰ",
"フィールド・ミュージアム研究Ⅱ",
"フィールド・ミュージアム研究Ⅲ",
"フィールド・ミュージアム演習Ⅰ",
"フィールド・ミュージアム演習Ⅱ"
], 12)
},
"英文学科 British and American Literature and Culture" :{
"English skills Ⅰ" : ([
"Reading Literature in English Ⅰ",
"Reading Literature in English Ⅱ",
"English Phonetics Ⅰ",
"English Phonetics Ⅱ",
"Basic Reading & Writing Ⅰ",
"Basic Reading & Writing Ⅱ",
"Listening & Speaking Ⅰ",
"Listening & Speaking Ⅱ",
"Discussion & Debate",
"Advanced Reading & Writing "
], 20),
"English skills Ⅱ" : ([
"English GrammarⅠ",
"English GrammarⅡ",
"Media EnglishⅠ (TV News）",
"Media EnglishⅡ (Magazines）",
"SpeechⅠ",
"SpeechⅡ",
"Advanced Discussion & Debate",
"Presentation",
"TOEIC WorkshopⅠ",
"TOEIC WorkshopⅡ",
"TOEFL Workshop",
"English through Drama",
"Current Issues in ESWⅠ",
"Current Issues in ESWⅡ",
"Business EnglishⅠ",
"Business EnglishⅡ",
"Hospitality EnglishⅠ",
"Hospitality EnglishⅡ",
"Translation"
], 8),
"World Englishes and Literature" : ([
"World EnglishesⅠ",
"World EnglishesⅡ",
"World LiteratureⅠ",
"World LiteratureⅡ",
"Japanese Literature in English",
"Classic Literature",
"Introducing Mt. FujiⅠ",
"Introducing Mt. FujiⅡ",
"Introducing JapanⅠ",
"Introducing JapanⅡ",
"Comparative CultureⅠ",
"Comparative CultureⅡ",
"Intercultural CommunicationⅠ",
"Intercultural CommunicationⅡ",
"Asian Literature in English",
"Children's Literature",
"Gender and SexualityⅠ",
"Gender and SexualityⅡ",
"Transnational LiteratureⅠ",
"Transnational LiteratureⅡ",
"Ethnic Minority LiteratureⅠ",
"Ethnic Minority LiteratureⅡ",
"Japonism",
"Cultural Studies",
], 10),
"British and American Literature and Culture" : ([
"History of British LiteratureⅠ",
"History of British LiteratureⅡ",
"History of American LiteratureⅠ",
"History of American LiteratureⅡ",
"Intro to British & American TheaterⅠ",
"Intro to British & American TheaterⅡ",
"British Culture and HistoryⅠ",
"British Culture and HistoryⅡ",
"American Culture and HistoryⅠ",
"American Culture and HistoryⅡ",
"Popular Culture",
"British and American Films",
"British NovelsⅠ",
"British NovelsⅡ",
"British TheaterⅠ",
"British TheaterⅡ",
"American NovelsⅠ",
"American NovelsⅡ",
"American TheaterⅠ",
"American TheaterⅡ",
"British and American Poetry",
], 20),
"Seminar" : ([
"Seminar in Literature and CultureⅠ",
"Seminar in Literature and CultureⅡ",
"Seminar in Literature and CultureⅢ",
"Seminar in Literature and CultureⅣ",
], 8),
"卒業論文" : ([
"卒業論文"
], 4),
"外国語科目" : ([
"English FoundationsⅠ",
"English FoundationsⅡ",
"English TELLⅠ",
"English TELLⅡ",
"EAP 1（Academic Listening, Discussion & Presentation) Ⅰ"
"EAP 1 （Academic Listening, Discussion & Presentation) Ⅱ"
"EAP 2 （Academic Reading & Writing) Ⅰ"
"EAP 2 （Academic Reading & Writing) Ⅱ"
"Advanced English TELL Ⅰ"
"Advanced English TELL Ⅱ"
"Extensive Reading"
"Intensive Reading"
"Movie English Ⅰ"
"Movie English Ⅱ"
"English for Business Ⅰ"
"English for Business Ⅱ"
"ドイツ語総合Ⅰ"
"ドイツ語総合Ⅱ"
"ドイツ語演習Ⅰ"
"ドイツ語演習Ⅱ"
"German Intermediate (B1) Ⅰ"
"German Intermediate (B1) Ⅱ"
"フランス語総合Ⅰ"
"フランス語総合Ⅱ"
"フランス語演習Ⅰ"
"フランス語演習Ⅱ"
"French Intermediate (B1) Ⅰ"
"French Intermediate (B1) Ⅱ"
"中国語総合Ⅰ"
"中国語総合Ⅱ"
"中国語演習Ⅰ"
"中国語演習Ⅱ"
"中国語応用演習Ⅰ"
"中国語応用演習Ⅱ"
"韓国朝鮮語総合Ⅰ"
"韓国朝鮮語総合Ⅱ"
"韓国朝鮮語演習Ⅰ"
"韓国朝鮮語演習Ⅱ"
"韓国朝鮮語応用演習Ⅰ"
"韓国朝鮮語応用演習Ⅱ""スペイン語総合Ⅰ"
"スペイン語総合Ⅱ"
"スペイン語演習Ⅰ"
"スペイン語演習Ⅱ"
"Spanish Intermediate（B1）Ⅰ"
"Spanish Intermediate（B1）Ⅱ"
"日本語アカデミック・プレゼンテーションⅠ"
"日本語アカデミック・プレゼンテーションⅡ"
"日本語アカデミック・ライティングⅠ"
"日本語アカデミック・ライティングⅡ"
"日本語読解Ⅰ"
"日本語読解Ⅱ"
"日本語能力総合演習Ⅰ"
"日本語能力総合演習Ⅱ"
"日本語総合研究活動Ⅰ"
"日本語総合研究活動Ⅱ"
"就職・仕事の日本語Ⅰ"
"就職・仕事の日本語Ⅱ"
"日本語待遇表現Ⅰ"
"日本語待遇表現Ⅱ"
], 8),
"教養科目" : ([
"アカデミック・スキルズ",
"自然と生命Ⅰ",
"自然と生命Ⅱ",
"自然と生命Ⅲ",
"自然と生命Ⅳ",
"自然と生命Ⅴ",
"自然と生命Ⅵ",
"自然と生命Ⅶ",
"世界と自己Ⅰ",
"世界と自己Ⅱ",
"世界と自己Ⅲ",
"世界と自己Ⅳ",
"世界と自己Ⅴ",
"世界と自己Ⅵ",
"世界と自己Ⅶ",
"世界と自己Ⅷ",
"世界と自己Ⅸ",
"世界と自己Ⅹ",
"日本国憲法",
"市民と社会Ⅰ",
"市民と社会Ⅱ",
"市民と社会Ⅲ",
"市民と社会Ⅳ",
"市民と社会Ⅴ",
"市民と社会Ⅵ",
"歴史と文化Ⅰ",
"歴史と文化Ⅱ",
"歴史と文化Ⅲ",
"歴史と文化Ⅳ",
"歴史と文化Ⅴ",
"歴史と文化Ⅵ",
"歴史と文化Ⅶ",
"歴史と文化Ⅷ",
"歴史と文化Ⅸ",
"現代の課題Ⅰ",
"現代の課題Ⅱ",
"現代の課題Ⅲ",
"現代の課題Ⅳ",
"現代の課題Ⅴ",
"現代の課題Ⅵ",
"現代の課題Ⅶ",
"現代の課題Ⅷ",
"デジタルシティズンシップ入門",
"データサイエンス（プログラミング）",
"データサイエンス（リテラシー）",
"データサイエンス（応用）",
"データサイエンス演習Ⅰ",
"データサイエンス演習Ⅱ",
"ジェンダー研究入門",
"ジェンダー研究への誘い",
"ジェンダー研究Ⅰ",
"ジェンダー研究Ⅱ",
"ジェンダー研究Ⅲ",
"ジェンダー研究Ⅳ",
"ジェンダー研究Ⅴ",
"ジェンダー研究Ⅵ",
"フィールド・ミュージアム入門",
"フィールド・ミュージアム研究Ⅰ",
"フィールド・ミュージアム研究Ⅱ",
"フィールド・ミュージアム研究Ⅲ",
"フィールド・ミュージアム演習Ⅰ",
"フィールド・ミュージアム演習Ⅱ"
], 12)
}}

certification = {
"中学英語" : {
    "必修科目" : [
    "教育原理",
    "教育関係法規",
    "教育心理学",
    "特別支援教育概論",
    "道徳の指導法",
    "総合的な学習の時間の指導法",
    "特別活動の指導法",
    "教育におけるICT活用",
    "学校相談心理学",
    "教職入門",
    "教育課程論（中等）",
    "教育方法論（中等）",
    "生徒・進路指導論（中等）",
    "中学教育実習",
    "教職実践演習",
    "介護等体験"],
    "教科及び教科の指導法に関する科目" : {
    "英語学" : (["English GrammarⅠ",
    "English PhoneticsⅠ",
    "Introduction to English LinguisticsⅠ",
    "Introduction to English LinguisticsⅡ"], 1),
    "英語文学" : (["Reading Literature in EnglishⅠ"], 1),
    "英語コミュニケーション" : (["Basic Reading & WritingⅠ",
    "Basic Reading & WritingⅡ",
    "Advanced Reading & Writing",
    "Listening & SpeakingⅠ",
    "Listening & SpeakingⅡ"], 1),
    "異文化理解" : (["Comparative CultureⅠ",
    "Intercultural CommunicationⅠ"], 1),
    "各教科の指導法" : (["TEFL（英語科教育法）Ⅰ",
    "TEFL（英語科教育法）Ⅱ",
    "TEFL（英語科教育法）Ⅲ",
    "TEFL（英語科教育法）Ⅳ"], 8),
    },
    "大学が独自に設定する科目" : ([
    "Introduction to SLA and ELTⅠ",
    "Introduction to SLA and ELTⅡ",
    "TEFL in PracticeⅡ",
    "Issues in TESOLⅠ",
    "Issues in TESOLⅡ",
    "World EnglishesⅠ"], 5)
    },
"高校英語" : {
    "必修科目" : [
    "教育原理",
    "教育関係法規",
    "教育心理学",
    "特別支援教育概論",
    "総合的な学習の時間の指導法",
    "特別活動の指導法",
    "教育におけるICT活用",
    "学校相談心理学",
    "教職入門",
    "教育課程論（中等）",
    "教育方法論（中等）",
    "生徒・進路指導論（中等）",
    "高校教育実習",
    "教職実践演習"],
    "教科及び教科の指導法に関する科目" : {
    "英語学" : (["English GrammarⅠ",
    "English PhoneticsⅠ",
    "Introduction to English LinguisticsⅠ",
    "Introduction to English LinguisticsⅡ"], 1),
    "英語文学" : (["Reading Literature in EnglishⅠ"], 1),
    "英語コミュニケーション" : (["Basic Reading & WritingⅠ",
    "Basic Reading & WritingⅡ",
    "Advanced Reading & Writing",
    "Listening & SpeakingⅠ",
    "Listening & SpeakingⅡ"], 1),
    "異文化理解" : (["Comparative CultureⅠ",
    "Intercultural CommunicationⅠ"], 1),
    "各教科の指導法" : (["TEFL（英語科教育法）Ⅰ",
    "TEFL（英語科教育法）Ⅱ",
    "TEFL（英語科教育法）Ⅲ",
    "TEFL（英語科教育法）Ⅳ"], 8),
    },
    "大学が独自に設定する科目" : ([
    "Introduction to SLA and ELTⅠ",
    "Introduction to SLA and ELTⅡ",
    "TEFL in PracticeⅡ",
    "Issues in TESOLⅠ",
    "Issues in TESOLⅡ",
    "World EnglishesⅠ"], 8)
    }
,
"中高英語" :  {
    "必修科目" : [
    "教育原理",
    "教育関係法規",
    "教育心理学",
    "特別支援教育概論",
    "道徳の指導法",
    "総合的な学習の時間の指導法",
    "特別活動の指導法",
    "教育におけるICT活用",
    "学校相談心理学",
    "教職入門",
    "教育課程論（中等）",
    "教育方法論（中等）",
    "生徒・進路指導論（中等）",
    "中等教育実習",
    "教職実践演習",
    "介護等体験"],
    "教科及び教科の指導法に関する科目" : {
    "英語学" : (["English GrammarⅠ",
    "English PhoneticsⅠ",
    "Introduction to English LinguisticsⅠ",
    "Introduction to English LinguisticsⅡ"], 1),
    "英語文学" : (["Reading Literature in EnglishⅠ"], 1),
    "英語コミュニケーション" : (["Basic Reading & WritingⅠ",
    "Basic Reading & WritingⅡ",
    "Advanced Reading & Writing",
    "Listening & SpeakingⅠ",
    "Listening & SpeakingⅡ"], 1),
    "異文化理解" : (["Comparative CultureⅠ",
    "Intercultural CommunicationⅠ"], 1),
    "各教科の指導法" : (["TEFL（英語科教育法）Ⅰ",
    "TEFL（英語科教育法）Ⅱ",
    "TEFL（英語科教育法）Ⅲ",
    "TEFL（英語科教育法）Ⅳ"], 8),
    },
    "大学が独自に設定する科目" : ([
    "Introduction to SLA and ELTⅠ",
    "Introduction to SLA and ELTⅡ",
    "TEFL in PracticeⅡ",
    "Issues in TESOLⅠ",
    "Issues in TESOLⅡ",
    "World EnglishesⅠ"], 8)
    }
}

def load_csv(csv_path):
    df = pd.read_csv(csv_path, skiprows = 8, usecols = [0,1,2,3,4,5,6,7,8,9], encoding = "cp932")
    df_filtered = df[~df["合否"].isin(["否"])]
    df_filled = df_filtered.ffill(axis = 1)
    return df_filled

def graduation_check(df_filled, selected_course):
    output_lines = []
    total_kyoka_credits = 0
    taken_subjects = df_filled["科目"].tolist()
    untaken_subjects = []
    result = df_filled.groupby("科目小区分")["単位数"].sum()

    if result.get("教養科目", 0) >= 16:
        result["教養科目"] = 16

    requirements = Department[selected_course]

    for category, (subject_list, req_credits) in requirements.items():
        earned = df_filled[df_filled["科目"].isin(subject_list)]["単位数"].sum()
        total_kyoka_credits += earned
        if earned >= req_credits:
            output_lines.append(f"{category} cleared")
        else:
            output_lines.append(f"{category} {req_credits - earned} remain")
            if category not in ["Seminar", "卒業論文"]:
                not_taken = [sub for sub in subject_list if sub not in taken_subjects]
                untaken_subjects.extend(not_taken)

    if result.sum() >= 124:
        output_lines.append(f"total cleared!")
    else:
        output_lines.append(f"total {124 - result.sum()} remain")

    return "\n".join(output_lines), untaken_subjects

def certification_check(df_filled, selected_certification):
    output_lines = []
    must_remain = 0
    total_kyoka_credits = 0
    cleared_category = 0
    requirements = certification[selected_certification]

    for credits in requirements["必修科目"]:
        if credits not in df_filled["科目"].values:
            output_lines.append(f"{credits} remain")
            must_remain += 1
    if must_remain == 0:
        output_lines.append(f"教職必修: clear")
        
    for category, (subject_list, req_credits) in requirements["教科及び教科の指導法に関する科目"].items():
        earned = df_filled[df_filled["科目"].isin(subject_list)]["単位数"].sum()
        total_kyoka_credits += earned
        if earned >= req_credits:
            cleared_category += 1
            output_lines.append(f"{category} cleared")
        else:
            output_lines.append(f"{category} {req_credits - earned} remain")
    if total_kyoka_credits >= 28 and cleared_category == 5:
        output_lines.append("教科及び教科の指導法（合計）: clear")

    uni_subjects, uni_req = requirements["大学が独自に設定する科目"]
    earned_uni = df_filled[df_filled["科目"].isin(uni_subjects)]["単位数"].sum()
    if earned_uni < uni_req:
        remain_uni = uni_req - earned_uni
        output_lines.append(f"大学が独自に設定する科目: {remain_uni} remain")
    else:
        output_lines.append("大学が独自に設定する科目: clear")


    return "\n".join(output_lines)

def load_classinfo():
    df_class = pd.read_csv("classinfo.csv", encoding = "utf-8")
    return df_class

def recommend_courses(df_class, untaken_subjects):
    if not untaken_subjects:
        return "すべての区分をクリアしています！"
    pattern = "|".join([f"(?:^|／){re.escape(sub)}" for sub in untaken_subjects])
    matched_df = df_class[df_class["開講科目名／Course"].str.contains(pattern, na=False)]
    matched_df = matched_df.drop_duplicates(subset=["開講科目名／Course"])
    exclude_words = "Seminar|専門演習|卒業論文|～2023入学"
    matched_df = matched_df[~matched_df["開講科目名／Course"].str.contains(exclude_words, na=False)]
    rec_lines = ["【おすすめ履修候補】"]
    for _, row in matched_df.iterrows():
        rec_lines.append(f"・{row['開講科目名／Course']}（{row['開講区分／semester offered']} / {row['曜限／Day&comma; Period']}）")

    return "\n".join(rec_lines)