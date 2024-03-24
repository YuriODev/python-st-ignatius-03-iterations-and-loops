class TestOutputFormatter:
    @staticmethod
    def get_failure_details_in_table(input_value: list, expected_output, actual_output) -> str:
        # Ensure the first line of input is considered in the table printing process
        input_value_str = '\n'.join(input_value)  # Convert list to string if needed

        # ANSI escape code for yellow
        yellow_start = "\x1b[38;5;208m"
        yellow_end = "\x1b[0m"
        # Print the "Failed test:" message
        output = f"\n{yellow_start}Failed test:{yellow_end}\n"

        # Find the longest output list for proper table formatting
        max_lines = max(len(expected_output), len(actual_output))
        max_length = max([len(input_value_str)] + [len(line) for line in expected_output + actual_output])
        column_width = max(max_length, len("| Expected Output |"))

        # Preparing the table border based on the longest content
        table_width = 3 * column_width + 9  # including padding and separators
        divider = yellow_start + "+" + "-" * (table_width - 1) + "+" + yellow_end

        # Printing the table headers and top border
        output += divider + "\n"
        header = f"| {'Input'.ljust(column_width)} | {'Expected Output'.ljust(column_width)} | {'Actual Output'.ljust(column_width)} |"
        output += yellow_start + header + yellow_end + "\n"
        output += divider + "\n"

        # Printing rows
        max_lines = max(len(input_value), len(expected_output), len(actual_output))
        for i in range(max_lines):
            row = "|"
            # Input value column
            if i < len(input_value):
                row += f" {input_value[i].ljust(column_width)} |"
            else:
                row += " " * (column_width + 2) + "|"

            # Expected and Actual Output columns
            for output_list in [expected_output, actual_output]:
                if i < len(output_list):
                    row += f" {output_list[i].ljust(column_width )} |"
                else:
                    row += " " * (column_width + 1) + "|"
            output += yellow_start + row + yellow_end + "\n"

        # Adding the bottom divider
        output += divider + "\n"

        return output

    @staticmethod
    def generate_loop_usage_message():
        """
        Generates a custom message in a table format about the misuse of loops.
        """
        yellow_start = "\x1b[38;5;208m"
        yellow_end = "\x1b[0m"
        message_lines = [
            "\n",
            yellow_start + "Failed test:" + yellow_end,
            yellow_start + "+-------------------------------------------------------+" + yellow_end,
            yellow_start + "|                     Loop Usage Error                  |" + yellow_end,
            yellow_start + "+-------------------------------------------------------+" + yellow_end,
            yellow_start + "| The solution must use a 'for' or 'while' loop.        |" + yellow_end,
            yellow_start + "+-------------------------------------------------------+" + yellow_end,
        ]
        return "\n".join(message_lines)
