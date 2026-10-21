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
"中学英語" : [
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
"介護等体験"
],
"高校英語" : [
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
"教育実践演習",
],
"中高英語" : [
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
"介護等体験"
]}

def load_csv(csv_path):
    df = pd.read_csv(csv_path, skiprows = 8, usecols = [0,1,2,3,4,5,6,7,8,9], encoding = "cp932")
    df_filtered = df[~df["合否"].isin(["否"])]
    df_filled = df_filtered.ffill(axis = 1)
    return df_filled

def guraduation_check(df_filled, selected_course):
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

def cirtification_check(df_filled, selected_course):
    output_lines = []
    requirements = certification[selected_course]

    for credits in requirements:
        if credits in df_filled["科目"].values:
            output_lines.append(f"{credits} cleared")
        else:
            output_lines.append(f"{credits} remain")

    return "\n".join(output_lines)


res = cirtification_check("kakuteiSeisekiCsv.csv", "中学英語")
print(res)