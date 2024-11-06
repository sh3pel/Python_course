def format_table(benchmarks, algos, results):
    m = max(len(max(benchmarks, key=len)), len(max(algos, key=len)), len(str(max(*max(*results)))))
    a = "| " +"Benchmark".center(m, " ") + " | " 
    l  = len(a)
    print(a, end="")
    for i in range(len(algos)):
        a = algos[i].center(m, " ") + " | "
        l += len(a)
        print(a, end="")
    print("\n" + "|" + "-" * (l - 3) + "|")
    for i in range(len(benchmarks)):
        a = "| " + benchmarks[i].center(m, " ") + " | "
        print(a, end="")
        for j in range(len(results)):
            for k in range(len(results[j])):
                a = str(results[j][k]).center(m, " ") + " | "
                print(a, end="")
            results.pop(j)
            break
        print()

format_table(["best case", "the worst case"],
["quick sort", "merge sort", "bubble sort"],
[[1.23, 1.56, 2.0], [3.3, 2.9, 3.9]])
print()
format_table(["best case", "worst case", "Average sssssmth"], ["quick sort", "merge sort", "bubble sort", "radix sort"],[[1.23, 1.56, 2.0, 0.01], [3.3, 2.9, 3.9, 1]])