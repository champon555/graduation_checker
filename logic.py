import pandas as pd

Department = {
"英文学科 English Linguistic and Education" : {
"English skills Ⅰ" : 20,
"English skills Ⅱ" : 8,
"World Englishes and Literature" : 10,
"English Linguistics and Education" : 20,
"Seminar" : 8,
"卒業論文" : 4,
"外国語科目" : 8,
"教養科目" : 12
},
"英文学科 British and American Literature and Culture" :{
"English skills Ⅰ" : 20,
"English skills Ⅱ" : 8,
"World Englishes and Literature" : 10,
"British and American Literature and Culture" : 20,
"Seminar" : 8,
"卒業論文" : 4,
"外国語科目" : 8,
"教養科目" : 12
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
    "教育実践演習",
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
    "World EnglishesⅠ"], 4)
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
    "教育実践演習"],
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
    "教育実践演習",
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
    result = df_filled.groupby("科目小区分")["単位数"].sum()

    if result.get("教養科目", 0) >= 16:
        result["教養科目"] = 16

    requirements = Department[selected_course]

    for category, req_credits in requirements.items():
        earned = result.get(category, 0)
        if earned >= req_credits:
            output_lines.append(f"{category} cleared")
        else:
            output_lines.append(f"{category} {req_credits - earned} remain")

    if result.sum() >= 124:
        output_lines.append(f"total cleared!")
    else:
        output_lines.append(f"total {124 - result.sum()} remain")

    return "\n".join(output_lines)

def certification_check(df_filled, selected_certification):
    output_lines = []
    total_kyoka_credits = 0
    cleared_category = 0
    requirements = certification[selected_certification]
    for credits in requirements["必修科目"]:
        if credits not in df_filled["科目"].values:
            output_lines.append(f"{credits} remain")
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