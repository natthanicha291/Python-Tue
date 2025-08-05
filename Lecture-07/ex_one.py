survey_result = [
    ["Python", "JavaScript", "C++"],
    ["Python", "JavaScript", "C#"],
    ["Python", "Java"],
    ["Python", "C++", "JavaScript"],
    ["Python", "JavaScript", "C++", "Java"],
]

choices_sets = [set(p) for p in survey_result]
common_languages = set.intersection(*choices_sets)
print("1.Languages chosen by all participants:", common_languages)

from collections import Counter
all_languages = [lang for participant in survey_result for lang in participant]
counts  = Counter(all_languages)

unique_to_one = {lang for lang, cnt in counts.items() if cnt == 1}
print("2.Languages only chosen by one participant:", unique_to_one)

unique_languages = set(all_languages)
print("3. Number of unique languages:", len(unique_languages))

chosen_by_two = {lang for lang, cnt in counts.items() if cnt == 2}
print("4.Languages chosen by exactly two paraticipants:", chosen_by_two)

duplicates = []
for i in range(len(choices_sets)):
    for j in range(i+1, len(choices_sets)):
        if choices_sets[i] == choices_sets[j]:
            duplicates.append([i+1, j+1])
print("5.Participants with the same set ot languages:", duplicates)