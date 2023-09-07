class Table:
    def __init__(self, headers, data):
        self.headers = headers
        self.data = data
        self.column_widths = self._calculate_column_widths()

    def __str__(self):
        table_str = self._generate_header() + self._generate_data()
        return table_str

    def _calculate_column_widths(self):
        column_widths = [len(header) for header in self.headers]
        for row in self.data:
            for i, cell in enumerate(row):
                width = len(str(cell))
                if width > column_widths[i]:
                    column_widths[i] = width
        return column_widths

    def _generate_header(self):
        header_str = "|"
        for i, header in enumerate(self.headers):
            header_str += f" {header:<{self.column_widths[i]}} |"
        header_str += "\n"
        header_str += "+"
        for width in self.column_widths:
            header_str += f"{'-' * (width + 2)}+"
        header_str += "\n"
        return header_str

    def _generate_data(self):
        data_str = ""
        for row in self.data:
            data_str += "|"
            for i, cell in enumerate(row):
                data_str += f" {str(cell):<{self.column_widths[i]}} |"
            data_str += "\n"
        return data_str

