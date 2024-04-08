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
    def generate_message(title: str, content: str) -> str:
        """
        Generates a custom message in a table format with the given title and content.
        """
        yellow_start = "\x1b[38;5;208m"
        yellow_end = "\x1b[0m"
        title_width = 70
        content_width = 70
        title_padding = (title_width - len(title)) // 2
        content_padding = (content_width - len(content)) // 2
        message_lines = [
            "\n",
            yellow_start + "Failed test:" + yellow_end,
            yellow_start + "+" + "-" * (title_width + 2) + "+" + yellow_end,
            yellow_start + f"| {' ' * title_padding}{title}{' ' * title_padding} |" + yellow_end,
            yellow_start + "+" + "-" * (title_width + 2) + "+" + yellow_end,
            yellow_start + f"| {' ' * content_padding}{content}{' ' * content_padding} |" + yellow_end,
            yellow_start + "+" + "-" * (content_width + 2) + "+" + yellow_end,
        ]
        return "\n".join(message_lines)

    @staticmethod
    def generate_loop_usage_message():
        """
        Generates a custom message in a table format about the misuse of loops.
        """
        title = "Loop Usage Error"
        content = "The solution must use a 'for' or 'while' loop."
        return TestOutputFormatter.generate_message(title, content)

    @staticmethod
    def generate_continue_usage_message():
        """
        Generates a custom message in a table format about the misuse of the 'continue' statement.
        """
        title = "Continue Usage Error"
        content = "The solution must use the 'continue' statement."
        return TestOutputFormatter.generate_message(title, content)

    @staticmethod
    def generate_if_usage_message():
        """
        Generates a custom message in a table format about the misuse of the 'if' statement.
        """
        title = "If Usage Error"
        content = "The solution must not use the 'if' statement."
        return TestOutputFormatter.generate_message(title, content)

    @staticmethod
    def generate_list_usage_message():
        """
        Generates a custom message in a table format about the misuse of lists.
        """
        title = "List Usage Error"
        content = "The solution must not use lists."
        return TestOutputFormatter.generate_message(title, content)

    @staticmethod
    def generate_string_slice_message():
        """
        Generates a custom message in a table format about the misuse of string slicing.
        """
        title = "String Usage Error"
        content = "The solution must not use string slicing on converting to str."
        return TestOutputFormatter.generate_message(title, content)

    @staticmethod
    def generate_division_by_zero_message():
        """
        Generates a custom message in a table format about division by zero.
        """
        title = "Division by Zero Error"
        content = "The solution must not divide by zero."
        return TestOutputFormatter.generate_message(title, content)

    @staticmethod
    def generate_math_module_usage_message():
        """
        Generates a custom message in a table format about the misuse of the 'math' module.
        """
        title = "Math Module Usage Error"
        content = "The solution must not use the 'math' module."
        return TestOutputFormatter.generate_message(title, content)

    @staticmethod
    def generate_modulo_division_by_zero_message():
        """
        Generates a custom message in a table format about the misuse of the modulo operator with zero.
        """
        title = "Modulo by Zero Error"
        content = "The solution must not use the modulo operator with zero."
        return TestOutputFormatter.generate_message(title, content)

    @staticmethod
    def generate_product_symbol_usage_message():
        """
        Generates a custom message in a table format about the misuse of the '*' symbol.
        """
        title = "Product Symbol Usage Error"
        content = "The solution must not use the '*' symbol to calculate the product."
        return TestOutputFormatter.generate_message(title, content)

    @staticmethod
    def generate_division_operator_usage_message():
        """
        Generates a custom message in a table format about the misuse of the division operator.
        """
        title = "Division Operator Usage Error"
        content = "The solution must not use the division operator."
        return TestOutputFormatter.generate_message(title, content)

    @staticmethod
    def generate_modulo_operator_usage_message():
        """
        Generates a custom message in a table format about the misuse of the modulo operator.
        """
        title = "Modulo Operator Usage Error"
        content = "The solution must not use the modulo operator."
        return TestOutputFormatter.generate_message(title, content)
    
    @staticmethod
    def generate_integer_division_operator_usage_message():
        """
        Generates a custom message in a table format about the misuse of the integer division operator.
        """
        title = "Integer Division Operator Usage Error"
        content = "The solution must not use integer division."
        return TestOutputFormatter.generate_message(title, content)

    @staticmethod
    def generate_sum_function_usage_message():
        """
        Generates a custom message in a table format about the misuse of the 'sum' function.
        """
        title = "Sum Function Usage Error"
        content = "The solution must not use the 'sum' function."
        return TestOutputFormatter.generate_message(title, content)

    @staticmethod
    def generate_range_function_usage_message():
        """
        Generates a custom message in a table format about the misuse of the 'range' function.
        """
        title = "Range Function Usage Error"
        content = "The solution must not use the 'range' function."
        return TestOutputFormatter.generate_message(title, content)
