# uncipher

## setup
to use this project, run 

    python3 ./subst_break.py --dict pth/to/a/standard/dict your_rot_encoded_string
    
## prerequisite
you need to have python3 installed on your computer, and to have a dict with one word per line, and only one word

here is a dict example : 
```
    A
    a
    aa
    ...
    zythum
    Zyzomys
    Zyzzogeton
    
```

    

## what does it do
It tries to decode your string by counting how many words it finds in the dict
with every possibility (26 counting the no substitution possibility)
