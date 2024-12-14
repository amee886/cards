import os
import random
import file_operations
from faker import Faker


FILENAME = "charsheet.svg"
os.makedirs("card", mode=0o777, exist_ok=False)
alphabet = { 'а': 'а͠', 'б': 'б̋', 'в': 'в͒͠',
 'г': 'г͒͠', 'д': 'д̋', 'е': 'е͠',
 'ё': 'ё͒͠', 'ж': 'ж͒', 'з': 'з̋̋͠',
 'и': 'и', 'й': 'й͒͠', 'к': 'к̋̋',
 'л': 'л̋͠', 'м': 'м͒͠', 'н': 'н͒',
 'о': 'о̋', 'п': 'п̋͠', 'р': 'р̋͠',
 'с': 'с͒', 'т': 'т͒', 'у': 'у͒͠',
 'ф': 'ф̋̋͠', 'х': 'х͒͠', 'ц': 'ц̋',
 'ч': 'ч̋͠', 'ш': 'ш͒͠', 'щ': 'щ̋',
 'ъ': 'ъ̋͠', 'ы': 'ы̋͠', 'ь': 'ь̋',
 'э': 'э͒͠͠', 'ю': 'ю̋͠', 'я': 'я̋',
 'А': 'А͠', 'Б': 'Б̋', 'В': 'В͒͠',
 'Г': 'Г͒͠', 'Д': 'Д̋', 'Е': 'Е',
 'Ё': 'Ё͒͠', 'Ж': 'Ж͒', 'З': 'З̋̋͠',
 'И': 'И', 'Й': 'Й͒͠', 'К': 'К̋̋',
 'Л': 'Л̋͠', 'М': 'М͒͠', 'Н': 'Н͒',
 'О': 'О̋', 'П': 'П̋͠', 'Р': 'Р̋͠',
 'С': 'С͒', 'Т': 'Т͒', 'У': 'У͒͠',
 'Ф': 'Ф̋̋͠', 'Х': 'Х͒͠', 'Ц': 'Ц̋',
 'Ч': 'Ч̋͠', 'Ш': 'Ш͒͠', 'Щ': 'Щ̋',
 'Ъ': 'Ъ̋͠', 'Ы': 'Ы̋͠', 'Ь': 'Ь̋',
 'Э': 'Э͒͠͠', 'Ю': 'Ю̋͠', 'Я': 'Я̋'
}
skill_list = ["Стремительный прыжок","Электрический выстрел","Ледяной удар","Стремительный удар","Кислотный взгляд",
        "Тайный побег","Ледяной выстрел","Огненный заряд"]


def main():
    for i in range(len(skill_list)):
        for old,new in alphabet.items():
                skill_list[i]=skill_list[i].replace(old,new)

            
    for i in range(10):
        with open(FILENAME,"r",encoding="utf-8") as file_:
            file=file_.read()
            fake=Faker("ru_RU")
            first_name=fake.first_name_male()
            last_name=fake.last_name_male()
            job=fake.job()
            town=fake.city()
            strength=random.randint(3,18)
            agility=random.randint(3,18)
            endurance=random.randint(3,18)
            intelligence=random.randint(3,18)
            luck=random.randint(3,18)
            skill=random.sample(skill_list,3)
            skill1=skill[0]
            skill2=skill[1]     
            skill3=skill[2]
            context={
                "first_name":first_name,
                "last_name":last_name,
                "job":job,
                "town":town,
                "strength":strength,
                "agility":agility,
                "endurance":endurance,
                "intelligence":intelligence,
                "luck":luck,
                "skill_1":skill1,
                "skill_2":skill2,
                "skill_3":skill3
                }
        
            RESULT = f"card\cards_{i+1}.svg"
            file_operations.render_template(FILENAME,RESULT,context)


if __name__=='__main__':
    main()
            