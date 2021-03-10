from difflib import SequenceMatcher,get_close_matches,Differ
str1="abcd"
str2="abcde"
seq=SequenceMatcher(a=str1,b=str2)
print(seq.ratio())


word_list=["abcdefg",'abcd','adef','cdea']
matches=get_close_matches(str1,word_list,n=2,cutoff=0.3)
print(matches)

