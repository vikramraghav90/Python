#Python 3.5.2 (default, Nov 12 2018, 13:43:14) 
#[GCC 5.4.0 20160609] on linux
#Type "help", "copyright", "credits" or "license" for more information.
#>>> 1 2
#  File "<stdin>", line 1
#    1 2
#      ^
#SyntaxError: invalid syntax
#>>> 1 2*
#  File "<stdin>", line 1
#    1 2*
#      ^
#SyntaxError: invalid syntax
#>>> 1 2* 6
#  File "<stdin>", line 1
#    1 2* 6
#      ^
#SyntaxError: invalid syntax
#>>> 1 * 6
#6
#>>> 1 *     ,6
#  File "<stdin>", line 1
#    1 *     ,6
#            ^
#SyntaxError: invalid syntax
#>>> 1 *     8+ 3
#11
#>>> 3 *     8+ 3
#27
#>>> 3 *     (8+ 3)
#33
#>>> 3 *     (8+ 3)+
#  File "<stdin>", line 1
#    3 *     (8+ 3)+
#                  ^
#SyntaxError: invalid syntax
#>>> 
