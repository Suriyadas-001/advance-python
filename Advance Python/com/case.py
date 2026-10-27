class string_cases:
    def str_upper(self,text):
        return text.upper()
    def str_lower(self,text):
        return text.lower()

str_case = string_cases()
print(str_case.str_upper("suriya"))

# if __name__ == "__main__":
#     str_case = string_cases()
#     print(str_case.str_upper("suriya"))