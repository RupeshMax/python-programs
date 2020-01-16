school={'ClassA':{'ram':{'eng':40,'sci':60,'maths':80},
                  'arun':{'eng':70,'sci':50,'maths':80},
                  'joy':{'eng':10,'sci':40,'maths':80}},
        'ClassB':{'hesh':{'eng':40,'sci':60,'maths':80},
                  'yash':{'eng':70,'sci':50,'maths':80},
                  'visu':{'eng':10,'sci':40,'maths':80}},
        'ClassB':{'dharu':{'eng':40,'sci':60,'maths':80},
                  'tom':{'eng':70,'sci':50,'maths':80},
                  'max':{'eng':10,'sci':40,'maths':80}}}

print(school)

print("1.List the students for the all the classes")
for k,v in school.items():
    print("{}{}{}".format(school[k],school[k+1],school[K+2]))
#for k,v in school.items():
