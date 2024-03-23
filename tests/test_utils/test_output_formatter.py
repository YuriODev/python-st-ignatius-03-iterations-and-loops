class TestOutputFormatter:
    @staticmethod
    def get_failure_details_in_table(input_value: list, expected_output, actual_output) -> str:

        # Convert the input list into a string
        input_value = '\n'.join(input_value)

        # ANSI escape code for yellow
        yellow_start = "\x1b[38;5;208m"
        yellow_end = "\x1b[0m"

        # Print the "Failed test:" message
        output = f"\n{yellow_start}Failed test:{yellow_end}\n"

        # Find the longest output list for proper table formatting
        max_lines = max(len(expected_output), len(actual_output))
        max_length = max([len(input_value)] + [len(line) for line in expected_output + actual_output])
        column_width = max_length + 2  # padding

        # Preparing the table border based on the longest content
        table_width = 3 * column_width + 9  # including padding and separators
        divider = yellow_start + "+" + "-" * (table_width - 1) + "+" + yellow_end

        # Printing the table headers and top border
        output += divider + "\n"
        header = f"| {'Input'.ljust(column_width)} | {'Expected Output'.ljust(column_width)} | {'Actual Output'.ljust(column_width)} |"
        output += yellow_start + header + yellow_end + "\n"
        output += divider + "\n"

        # Iterating over the maximum number of lines and printing each row
        for i in range(max_lines):
            exp = expected_output[i] if i < len(expected_output) else ""
            act = actual_output[i] if i < len(actual_output) else ""
            if i == 0:
                row = f"| {input_value.ljust(column_width)} | {exp.ljust(column_width)} | {act.ljust(column_width)} |"
            else:
                row = f"| {''.ljust(column_width)} | {exp.ljust(column_width)} | {act.ljust(column_width)} |"
            output += yellow_start + row + yellow_end + "\n"

        # Printing the bottom border
        output += divider + "\n"

        return output

