#Пришло время написать программу foobar. На вход получаете целое число, на выход foo, если число делится на 3, bar если делится на 5, foobar если и на 3 и на 5

a=int(input("введите целое число "))
print("foo"*(a%3==0)+"bar"*(a%5==0))
