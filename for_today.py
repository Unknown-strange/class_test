wedding_lists = ["kofi@gmail.com","AMA@gmail.com","Prince@gmail.com"]
print(wedding_lists)

wedding_lists.sort()

wedding_lists.append("edwin@gmail.com")
wedding_lists.remove("kofi@gmail.com")
lengh_of_list = len(wedding_lists)
new_wedding_list = []
print(lengh_of_list)
for wedding_list in wedding_lists:
    wedding_list =str(wedding_list)
    wedding_list = wedding_list.lower()
    new_wedding_list.append(wedding_list)
print(new_wedding_list)
