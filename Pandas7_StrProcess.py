import pandas as pd

# Pandas中要确保 Series 或者 DataFrame 的 dtype="string"
py_s = "A,B,C,Aaba,Baca,CABA,dog,cat"
pd_s = pd.Series(
    ["A", "B", "C", "Aaba", "Baca", "CABA", "dog", "cat"],
    dtype="string")

print("python:\n", py_s.upper())
print("\npandas:\n", pd_s.str.upper())

# 调整string格式
pd_not_s = pd.Series(
    ["A", "B", "C", "Aaba", "Baca", "CABA", "dog", "cat"],
)
print("pd_not_s type:", pd_not_s.dtype)
pd_s = pd_not_s.astype("string")
print("pd_s type:", pd_s.dtype)

# 对比原生python
print("python lower:\n", py_s.lower())
print("\npandas lower:\n", pd_s.str.lower())
print("python len:\n", [len(s) for s in py_s.split(",")])
print("\npandas len:\n", pd_s.str.len())

# 对比文字裁剪
py_s = ["   jack", "jill ", "    jesse    ", "frank"]
pd_s = pd.Series(py_s, dtype="string")
print("python strip:\n", [s.strip() for s in py_s])
print("\npandas strip:\n", pd_s.str.strip())

print("\n\npython lstrip:\n", [s.lstrip() for s in py_s])
print("\npandas lstrip:\n", pd_s.str.lstrip())

print("\n\npython rstrip:\n", [s.rstrip() for s in py_s])
print("\npandas rstrip:\n", pd_s.str.rstrip())

# 对比split拆分
py_s = ["a_b_c", "jill_jesse", "frank"]
pd_s = pd.Series(py_s, dtype="string")
print("python split:\n", [s.split("_") for s in py_s])
print("\npandas split:\n", pd_s.str.split("_"))

# 对于DataFrame，先选一个column 或者 row，拿到一个 Series 再开始做 str 的处理
pd_df = pd.DataFrame([["a", "b"], ["C", "D"]])
pd_df.iloc[0, :].str.upper()

# 正则表达式
pattern = r"[0-9][a-z]"
s = pd.Series(["1", "1a", "11c", "abc"], dtype="string")
s.str.contains(pattern)
# 只要包含正则规则，contains 就为 True， 但是 match() 的意思是你的正则规则要完全匹配才会返回 True。
pattern = r"[0-9]+?[a-z]"
s.str.match(pattern)

# replace
py_s = ["1", "1a", "21c", "abc"]
pd_s = pd.Series(py_s, dtype="string")
print("py_s replace '1' -> '9':\n", [s.replace("1", "9") for s in py_s])

print("\n\npd_s replace '1' -> '9':\n", pd_s.str.replace("1", "9"))
print("pd_s replace -> 'NUM':")
pd_s.str.replace(r"[0-9]", "NUM", regex=True)

# 拼接
s1 = pd.Series(["A", "B", "C", "D"], dtype="string")
s2 = pd.Series(["1", "2", "3", "4"], dtype="string")
s1.str.cat(s2)

