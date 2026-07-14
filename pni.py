class PrintConfig:
    def __init__(self):
        self.content = ''

    def add_content(self, content):
        if self.content == '':
            self.content = content
        else:
            self.content += '\n' + content

    def delete_content(self):
        self.content = ''

    def print_now(self):
        print(self.content)
    
    def get_input(self):
        return input(self.content)

if __name__ == "__main__":
    std = PrintConfig()
    std.add_content("Hello World!")
    std.print_now()
    std.delete_content()
    std.print_now()