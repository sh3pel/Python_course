def format_table(benchmarks, algos, results):
    if len(results) != len(benchmarks):
        raise ValueError("Количество результатов не соответствует количеству бенчмарков")

    benchmark_width = max(len(b) for b in benchmarks)
    algo_width = max(len(a) for a in algos)
    result_width = max(len(str(r)) for row in results for r in row)

    column_width = max(benchmark_width, algo_width, result_width)

    header = "| " + "Benchmark".ljust(column_width) + " | "
    for algo in algos:
        header += algo.ljust(column_width) + " | "
    print(header)

    separator = "|" + "-" * (column_width + 2) + "|"
    for _ in algos:
        separator += "-" * (column_width + 2) + "|"
    print(separator)

    for i, benchmark in enumerate(benchmarks):
        row = "| " + benchmark.ljust(column_width) + " | "
        for result in results[i]:
            row += str(result).ljust(column_width) + " | "
        print(row)

try:
    format_table(
        ["best case", "the worst case"],
        ["quick sort", "merge sort", "bubble sort"],
        [[1.23, 1.56, 2.0], [3.3, 2.9, 3.9]]
    )
except ValueError as e:
    print(e)
