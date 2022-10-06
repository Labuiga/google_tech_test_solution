This code finds the combinations between pairs of integers from two groups (a, b) whose sum is a specific integer (n):


    a = [1,2,3,5,6,9]
    b = [1,2,4,8]
    n = 8
    result = [(2,6), (3, 5)]

moreover, we can choose don't take the combinations within the same group (using ac=False), then:

    result = [(2,6)]

*details*: 0 is an integuer

---

USER GUIDE:

    cd google_tech_test_solution

Then, if u want to use the code arrays:

    python main.py

Or if You want to use a specific parameters, You can use -a, -b, -n, -ac with: 

    python main.py -a=[4,5,8] -b=[7,6,9], -n=9
    python main.py -a=[4,5,8] -b=[7,6,9], -n=9 -ac=False

Maybe you want to thest a group of parameters using file.json with:

    python main.py -f=True