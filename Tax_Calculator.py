### Introduction to the program:
print()
print(f"{'WELCOME TO EX+RA FAST CALCULATOR':^100}")
print()
# This code will greet the user according to the time setting of system:
import time
time_1 = int(time.strftime('%H'))
if (time_1>=5) and (time_1<=10):
    print('GOOD MORNING!')
elif (time_1>=11) and (time_1<=14):
    print('GOOD AFTER NOON!')
elif (time_1>=15) and (time_1<=18):
    print('GOOD EVENING!')
elif (time_1>=19) and (time_1<=23):
    print('GOOD NIGHT!')
else:
    print("How is your MIDNIGHT!")
print("Dear user.")

name = input("What is your name?   ")
print()
print(f"So Mr.{name.title()}, Let me introduce you with us.\n\t"
      "This is an income tax calculator, as per the income tax act, 1961.\n\t"
      "And, the rules and slab rates of old tax regime of the indian government.")

## Taking and checking the consent of user, whether he or she wants to proceed with the program:
print()
consent = input("\nAre you here for the same purpose?   ")

if (consent.lower() == 'yes') or (consent.lower() == 'yeah') or (consent.lower() == 'ofcourse'):

## Now, if the user is ready to go with us, then asking for the required details:
    print()
    print(f"GOOD {name.title()}!\n\tThen fill the following required details below:\n"
          f"Remember one thing, the details should belongs to the current year.")

## Assessing the details of income source of user:
    print()
    print(f'{" ":->90}')
    print("First of all, let me know your all sources of income:")
    print(f'{" ":->90}')
    Income_from_salary = float(input(f"{'Your monthly salary i.e,Sum of your '
                                        'Basic salary, HRA, LTA, DA allowances etc.':<80}|    ")) * 12
    basic_salary = float(input(f"{' ':>20}{'Basic salary':<23}|  ")) * 12
    HRA = float(input(f"{' ':>20}{'House Rent Allowance':<23}|  ")) * 12
    LTA = float(input(f"{' ':>20}{'Leave travel allowance':<23}|  ")) * 12
    DA = float(input(f"{' ':>20}{'Dearness allowance':<23}|  ")) * 12
    CA = float(input(f"{' ':>20}{'Conveyance allowance':<23}|  ")) * 12
    other_allowance = float(input(f"{' ':>20}{'Other allowance':<23}|  ")) * 12
    if (basic_salary + HRA + LTA + DA + CA + other_allowance) != Income_from_salary:
        print("Dear user, You are providing the wrong info about your salary component.\n"
              "Your total salary does not match with the total of your salary component.\n"
              " check the details and try again.")
    else:
        print(f'{" ":->90}')
        Income_from_house_rent = float(input(f"{'Monthly Income from house property (if any).'
                                                'like, rental income etc.':<80}|    ")) * 12
        print(f'{" ":->90}')
        Income_form_personal_business = float(input(f"{'Total annual Income from own business and profession (if any),'
                                                       ' i.e, Net income.':<80}|    "))
        print(f'{" ":->90}')
        capital_gain_or_loss = float(input(f"{'Total Profit or loss from sale of capital assets (if any).like, profit or loss':<80}|\n"
                                           f"{'from sale of shares, property, other short or long term asset, in current year.':<80}|    "))
        print(f'{" ":->90}')
        Income_form_other_source = float(input(f"{'Monthly Income from other source (if any).like, interest income,'
                                                  'dividends etc.':<80}|    ")) * 12
        print(f'{" ":->90}')

    ## calculating the GTI (Gross total income) of user:
        GTI = (Income_from_salary + Income_form_personal_business + Income_form_other_source
               + Income_from_house_rent + capital_gain_or_loss)

    ## Applying the exemptions:
        print(f'\n{'USER INFORMATION REGARDING EXEMPTIONS':^80}')
        print(f"Now Mr.{name.title()}, let me inform you, As per section 10 of the income tax act, 1961\n"
              "Some specific portion of your salary income (i.e, income from HRA, DA, TA allowances etc.)\n"
              "is exempted from tax calculation, that is determined according to the specified rules.\n"
              "So, You can claim these exemptions, by supplying the following details accurately, and\n"
              "minimize your taxable income.")
        print()
        print(f'{" ":->90}')
        rent_paid = float(input(f"{'The amount of rent paid (Monthly), to the household':<80}|   ")) * 12
        print(f'{" ":->90}')
        city_type = (input(f"{'Type of city, where you currently live. (Metro or Non-metro)':<80}|    "))
        print(f'{" ":->90}')
        no_of_children = int(input(f'{"The number of children you have.":<80}|    '))
        print(f'{" ":->90}')
        gratuity_received = float(input(f"{'The amount of gratuity received in current year (if any).':<80}|\n"
                                        f"{'Note: Do not provide this detail, if the amount of gratuity '
                                           'received in current':<80}|\n"
                                        f"{'year, is not included in you salary income.':<80}|    "))
    ##  Calculating the exemptions from the above details:
        HRA_exemption = min(HRA, 0.5*(basic_salary + DA) if city_type.lower() == 'metro'
                            else 0.4*(basic_salary + DA), rent_paid - (0.1* (basic_salary + DA)))
        print(f'{" ":->90}')
        LTA_exemption = LTA
        CA_exemption = min(CA, (1600*12))
        children_education_exemption = (min(no_of_children,2) * 100 * 12)
        gratuity_exemption = min(gratuity_received, 2000000)

        Total_exemption = (HRA_exemption + LTA_exemption + CA_exemption + children_education_exemption +
                           gratuity_exemption)
        Net_salary = (GTI - Total_exemption)

### Applying deductions:
        print()
        print(f"{'USER INFORMATION ABOUT DEDUCTION':^80}")
        print(f"Now Mr.{name.title()}, let me inform you about the deduction. According to the income tax act, 1961\n"
              f"Some specific type of expenditure are excluded form income for tax-calculation. if you have\n"
              f"incur such type of expenditures then you can minimize your taxable income and get the tax-relief.\n"
              f"So, kindly supply the following information, so that, we can determine the eligible deduction.")
        print()
        print(f'{" ":->90}')
        investment_80c = float(input(f"{'Amount of investment in the funds specified under section 80C. (if any)':<80}|\n"
                                     f"{'The section 80C includes:':<80}|\n"
                                     f"{'\t\t investment like PPF, ELSS, NSC, life insurance premium, 5-year FD,':<74}|\n"
                                     f"{'\t\t tuition fees for children, principal repayment of home loan.':<74}|    "))
        deduction_under_80c = min(investment_80c,150000)
        print(f'{" ":->90}')
        section_80d = float(input(f"{'Amount of health insurance premium for self, suppose, and dependent-children.':<80}|    "))
        print(f'{" ":->90}')
        insurnce_for_parents = float(input(f"{'Amount of health insurance for your parents. (if any)':<80}|    "))
        print(f'{" ":->90}')
        parents_age = int(input(f"{'Age of your parent (for whom you have bought the insurnce policy.)':<80}|    "))
        print(f'{" ":->90}')
        deduction_under_80d = min(section_80d, 25000)+ min(insurnce_for_parents, 50000 if parents_age >= 80
                                                           else 25000)
        deduction_under_80e = float(input(f"{'Amount of monthly interest for any educational loan. (if any)':<80}|    ")) * 12
        print(f'{" ":->90}')
        deduction_under_80g = float(input(f"{'Amount of donation to any charitable organisation. (if any)':<80}|    "))
        print(f'{" ":->90}')
        section_80tta = float(input(f"{'Total amount of saving account interest for the current year.':<80}|    "))
        print(f'{" ":->90}')
        deduction_under_80tta = min(section_80tta,10000)
        deduction_under_80gg = 0 ## search for its calculation then perform here.
        section_24 = float(input(f"{'Amount of monthly interest on home loan. (if any)':<80}|    ")) * 12
        print(f'{" ":->90}')
        possession = input(f"{'The possession above home is rented or self_occupied.':<80}|    ")
        print(f'{" ":->90}')
        deduction_under_24 = section_24 if possession.lower() == 'rented' else min(section_24, 200000)
        print("\nDeclaration:")
        declaration = input(f"\tI Mr.{name.title()}, hereby declare that the information i have provided\n"
                             f"above is true and correct in the best of my knowledge. (True or false)  ")
        if declaration.lower() == 'false':
            print(f"If the information you provide is wrong in your belief, then it may cause\n"
                  f"wrong calculation of income tax.")
            input("Got it?  ")

    ## Calculating total deduction:
        total_deduction = (deduction_under_80c + deduction_under_80d + deduction_under_80e +
                           deduction_under_80g + deduction_under_80tta + deduction_under_80gg + deduction_under_24)
        total_taxable_income = (Net_salary - total_deduction)

    ### Now, calculating tax by showing steps:
        print()
        print(f'\nOK {name.title()}, according to the details provided by you, your taxable income is as follows:')
        print()
        print(f"{'Taxable Income Calculation Chart':^105}")
        print(f"{"-":->105}")
        print(f"|{'S.no.':^6}|{'Particular':^80}|{'Amount':^15}|")
        print(f"{"-":->105}")
        print(f"|{'I.':^6}|{'Total income from different sources':<80}|{GTI:^15}|")
        print(f"|{'II.':^6}|{'Less: Exemptions':<80}|{'-':->15}|")
        print(f"|{'--':^6}|{' ':>5}{'Exemption for Home rent allowance (HRA)':<75}|{HRA_exemption:^15}|")
        print(f"|{'--':^6}|{' ':>5}{'Exemption for Leave travel allowance (LTA)':<75}|{LTA_exemption:^15}|")
        print(f"|{'--':^6}|{' ':>5}{'Exemption for Conveyance allowance (CA)':<75}|{CA_exemption:^15}|")
        print(f"|{'--':^6}|{' ':>5}{'Exemption for Children education allowance':<75}|{children_education_exemption:^15}|")
        print(f"|{'--':^6}|{' ':>5}{'Exemption for Gratuity exemption (GE)':<75}|{gratuity_exemption:^15}|")
        print(f"{"-":->105}")
        print(f"|{'III.':^6}|{'Net income':<80}|{Net_salary:^15}|")
        print(f"|{'IV.':^6}|{'Less: Deductions':<80}|{'-':->15}|")
        print(f"|{'--':^6}|{' ':>5}{'Deduction under section 80C':<75}|{deduction_under_80c:^15}|")
        print(f"|{'--':^6}|{' ':>5}{'Deduction under section 80D':<75}|{deduction_under_80d:^15}|")
        print(f"|{'--':^6}|{' ':>5}{'Deduction under section 80E':<75}|{deduction_under_80e:^15}|")
        print(f"|{'--':^6}|{' ':>5}{'Deduction under section 80G':<75}|{deduction_under_80g:^15}|")
        print(f"|{'--':^6}|{' ':>5}{'Deduction under section 80TTA':<75}|{deduction_under_80tta:^15}|")
        print(f"|{'--':^6}|{' ':>5}{'Deduction under section 80GG':<75}|{deduction_under_80gg:^15}|")
        print(f"|{'--':^6}|{' ':>5}{'Deduction under section 24':<75}|{deduction_under_24:^15}|")
        print(f"{"-":->105}")
        print(f"|{'V.':^6}|{'Total taxable income':^80}|{total_taxable_income:^15}|")
        print(f"{"-":->105}")

        ### Now, calculation of income tax as per the age-rules and applicable slab rate:
        print()
        print(f'\nNow mr.{name.title()}, we will calculate the amount of your income tax, as per the age-rules\n'
        f'and applicable slab rate of income tax act.')
        print()
        age = int(input(f"So please {name.title()}, Enter your age.   "))
        if age <= 60:
            age_category= "Below 60 year age group"
        elif (age > 60) and (age <= 80):
            age_category = 'Senior citizen group'
        else:
            age_category = 'Super senior citizen group'
        print(f'\nSo, Mr.{name.title()} You are under the {age_category}. So the calculation of income tax,\n'
                  f'as per the applicable slab rate to you, is as follows:')

        ### For showing calculation process with format:
        print()
        print(f"{'Income Tax Calculation Chart':^105}")
        S_no = ('I.', 'II.', 'III.', 'IV.','V.')

        ## Defining function for easy calculation:
        def perc(income, t_rate):
            if income == 0:
                return 0
            return (income * t_rate)/100

        ## For first age group
        if age_category == "Below 60 year age group":
            Category = ('0 - 250,000', '250,001 - 500,000', '500,001 - 10,00,000','Above 10,00,000')
            rate = ('0%', '5%', '20%', '30%')
            calculation = ('250000 x 0% = 0','250000 x 5% = 12500', '500000 x 20% = 100000')
            a = f'|{S_no[0]:^6}|{Category[0]:^30}|{rate[0]:^25}|{calculation[0]:^35}|'
            b = f'|{S_no[1]:^6}|{Category[1]:^30}|{rate[1]:^25}|{calculation[1]:^35}|'
            c = f'|{S_no[2]:^6}|{Category[2]:^30}|{rate[2]:^25}|{calculation[2]:^35}|'
            e = perc(250000,0)
            f = perc(250000,5)
            g = perc(500000,20)

            if total_taxable_income <= 250000:
                print(f'{"":->100}')
                print(f'|{'S_no.':^6}|{'Income category':^30}|{'Slab rate':^25}|{'Tax_calculation':^35}|')
                print(f'{"":->100}')
                print(f'{a}')
                print(f'{"":->100}')
                print(f"|{'II.':^6}|{'Total income tax':^56}={f'{e:.2f}':^35}|")
                print(f'{"":->100}')
                print()
                print(f"Mr.{name.title()}, your annual income do not fall into any taxable category.\n"
                      f"As per the slab rate for {age_category} of the old tax regime,\n"
                      "the income upto 250,000 rupees is exempted for tax.")
                print("\n\t So, your tax payable liability for this year is: 0")
            else:
                print(f'{"":->100}')
                print(f'|{'S_no.':^6}|{'Income category':^30}|{'Slab rate':^25}|{'Tax_calculation':^35}|')
                print(f'{"":->100}')
                print(f'{a}')
                print(f'{"":->100}')
                if (total_taxable_income > 250000) and (total_taxable_income <= 500000):
                    step_1 = (total_taxable_income - 250000)
                    step_2 = perc(total_taxable_income - 250000, 5)
                    result = (e + step_2)
                    print(f'|{S_no[1]:^6}|{Category[1]:^30}|{rate[1]:^25}|{f'{step_1} x 5% = {step_2}':^35}|')
                elif (total_taxable_income > 500000) and (total_taxable_income <= 1000000):
                    step_1 = (total_taxable_income - 500000)
                    step_2 = perc(total_taxable_income - 500000, 20)
                    result = (e + f + step_2)
                    print(f'{b}')
                    print(f'{"":->100}')
                    print(f'|{S_no[2]:^6}|{Category[2]:^30}|{rate[2]:^25}|{f'{step_1} x 20% = {step_2}':^35}|')
                elif total_taxable_income > 1000000:
                    step_1 = (total_taxable_income - 1000000)
                    step_2 = perc(total_taxable_income - 1000000, 30)
                    result = (e + f + g + step_2)
                    print(f'{b}')
                    print(f'{"":->100}')
                    print(f'{c}')
                    print(f'{"":->100}')
                    print(f'|{S_no[3]:^6}|{Category[3]:^30}|{rate[3]:^25}|{f'{step_1} x 30% = {step_2}':^35}|')
                print(f'{"":->100}')
                print(f"|{S_no[4]:^6}|{'Total income tax':^56}={f'{result:.2f}':^35}|")
                print(f'{"":->100}')

        ## For second age group
        elif age_category == "Senior citizen group":
            Category = ('0 - 300,000', '300,001 - 500,000', '500,001 - 10,00,000', 'Above 10,00,000')
            rate = ('0%', '5%', '20%', '30%')
            calculation = ('300000 x 0% = 0', '200000 x 5% = 10000', '500000 x 20% = 100000')
            a = f'|{S_no[0]:^6}|{Category[0]:^30}|{rate[0]:^25}|{calculation[0]:^35}|'
            b = f'|{S_no[1]:^6}|{Category[1]:^30}|{rate[1]:^25}|{calculation[1]:^35}|'
            c = f'|{S_no[2]:^6}|{Category[2]:^30}|{rate[2]:^25}|{calculation[2]:^35}|'
            e = perc(300000, 0)
            f = perc(200000, 5)
            g = perc(500000, 20)

            if total_taxable_income <= 300000:
                print(f'{"":->100}')
                print(f'|{'S_no.':^6}|{'Income category':^30}|{'Slab rate':^25}|{'Tax_calculation':^35}|')
                print(f'{"":->100}')
                print(f'{a}')
                print(f'{"":->100}')
                print(f"|{'II.':^6}|{'Total income tax':^56}={f'{e:.2f}':^35}|")
                print(f'{"":->100}')
                print()
                print(f"Mr.{name.title()}, your annual income do not fall into any taxable category.\n"
                      f"As per the slab rate for {age_category} of the old tax regime,\n"
                      "the income upto 300,000 rupees is exempted for tax.")
                print("\n\t So, your tax payable liability for this year is: 0")
            else:
                print(f'{"":->100}')
                print(f'|{'S_no.':^6}|{'Income category':^30}|{'Slab rate':^25}|{'Tax_calculation':^35}|')
                print(f'{"":->100}')
                print(f'{a}')
                print(f'{"":->100}')
                if (total_taxable_income > 300000) and (total_taxable_income <= 500000):
                    step_1 = (total_taxable_income - 300000)
                    step_2 = perc(total_taxable_income - 300000, 5)
                    result = (e + step_2)
                    print(f'|{S_no[1]:^6}|{Category[1]:^30}|{rate[1]:^25}|{f'{step_1} x 5% = {step_2}':^35}|')
                elif (total_taxable_income > 500000) and (total_taxable_income <= 1000000):
                    step_1 = (total_taxable_income - 500000)
                    step_2 = perc(total_taxable_income - 500000, 20)
                    result = (e + f + step_2)
                    print(f'{b}')
                    print(f'{"":->100}')
                    print(f'|{S_no[2]:^6}|{Category[2]:^30}|{rate[2]:^25}|{f'{step_1} x 20% = {step_2}':^35}|')
                elif total_taxable_income > 1000000:
                    step_1 = (total_taxable_income - 1000000)
                    step_2 = perc(total_taxable_income - 1000000, 30)
                    result = (e + f + g + step_2)
                    print(f'{b}')
                    print(f'{"":->100}')
                    print(f'{c}')
                    print(f'{"":->100}')
                    print(f'|{S_no[3]:^6}|{Category[3]:^30}|{rate[3]:^25}|{f'{step_1} x 30% = {step_2}':^35}|')
                print(f'{"":->100}')
                print(f"|{S_no[4]:^6}|{'Total income tax':^56}={f'{result:.2f}':^35}|")
                print(f'{"":->100}')

        ## For third age group:
        else:       ## age_group = 'super_senior_citizen'
            Category = ('0 - 500,000', '500,001 - 10,00,000', 'Above 10,00,000')
            rate = ('0%', '20%', '30%')
            calculation = ('500000 x 0% = 0', '500000 x 20% = 100000')
            a = f'|{S_no[0]:^6}|{Category[0]:^30}|{rate[0]:^25}|{calculation[0]:^35}|'
            b = f'|{S_no[1]:^6}|{Category[1]:^30}|{rate[1]:^25}|{calculation[1]:^35}|'
            c = f'|{S_no[2]:^6}|{Category[2]:^30}|{rate[2]:^25}|'
            d = perc(500000, 0)
            e = perc(500000, 20)

            if total_taxable_income <= 500000:
                print(f'{"":->100}')
                print(f'|{'S_no.':^6}|{'Income category':^30}|{'Slab rate':^25}|{'Tax_calculation':^35}|')
                print(f'{"":->100}')
                print(f'{a}')
                print(f'{"":->100}')
                print(f"|{'II.':^6}|{'Total income tax':^56}={f'{d:.2f}':^35}|")
                print(f'{"":->100}')
                print()
                print(f"Mr.{name.title()}, your annual income do not fall into any taxable category.\n"
                      f"As per the slab rate for {age_category} of the old tax regime,\n"
                      "the income upto 500,000 rupees is exempted for tax.")
                print("\n\t So, your tax payable liability for this year is: 0")
            else:
                print(f'{"":->100}')
                print(f'|{'S_no.':^6}|{'Income category':^30}|{'Slab rate':^25}|{'Tax_calculation':^35}|')
                print(f'{"":->100}')
                print(f'{a}')
                print(f'{"":->100}')
                if (total_taxable_income > 500000) and (total_taxable_income <= 1000000):
                    step_1 = (total_taxable_income - 500000)
                    step_2 = perc(total_taxable_income - 500000, 20)
                    result = (d + step_2)
                    print(f'|{S_no[1]:^6}|{Category[1]:^30}|{rate[1]:^25}|{f'{step_1} x 20% = {step_2}':^35}|')
                elif total_taxable_income > 1000000:
                    step_1 = (total_taxable_income - 1000000)
                    step_2 = perc(total_taxable_income - 1000000, 30)
                    result = (d + e + step_2)
                    print(f'{b}')
                    print(f'{"":->100}')
                    print(f'|{S_no[2]:^6}|{Category[2]:^30}|{rate[2]:^25}|{f'{step_1} x 30% = {step_2}':^35}|')
                print(f'{"":->100}')
                print(f"|{S_no[3]:^6}|{'Total income tax':^56}={f'{result:.2f}':^35}|")
                print(f'{"":->100}')

### Now, applying rebate, surcharge, and cess on calculated income tax:
        if total_taxable_income <= 500000:  # For applying rebate
            print(f'|{'Less: Rebate under section 87A (for income upto 5 lakh)':<63}={result:^35}|')
            print(f'|{'It means, no tax will be charged to individual with an income':<63}|{'|':>36}\n'
                  f'|{'of upto rupees 5 lakh, does\'nt matter the individual belong':<63}|{'|':>36}\n'
                  f'|{'to which age category, slab rate and so on.':<63}|{'|':>36}')
            print(f"|{'-':>64}{"-":->35}|")
            print(f"|{'Tax after rebate under section 87A':^63}={'0.00':^35}|")
            print(f'{"":->100}')
            total_tax = 0

        elif total_taxable_income > 500000:
            if (total_taxable_income >= 5000000) and (total_taxable_income < 10000000):
                print(f'|{'Add: Surcharge (an extra charge, other than tax) at the rate,':<63}|{" ":>35}|\n'
                      f'|{'of 10% of basic tax for income "50 lakh <= income < 1 crore"':<63}|'
                      f'{f'{result} x 10% = {perc(result, 10):.2f}':^35}|')
                surcharge = perc(result, 10)
            elif (total_taxable_income >= 10000000) and (total_taxable_income < 20000000):
                print(f'|{'Add: Surcharge (an extra charge, other than tax) at the rate':<63}|{" ":>35}|\n'
                      f'|{'of 15% of basic tax for income "1 crore <= income < 2 crore"':<63}|'
                      f'{f'{result} x 15% = {perc(result, 15):.2f}':^35}|')
                surcharge = perc(result, 15)
            elif (total_taxable_income >= 20000000) and (total_taxable_income < 50000000):
                print(f'|{'Add: Surcharge (an extra charge, other than tax) at the rate':<63}|{" ":>35}|\n'
                      f'|{'of 25% of basic tax for income "2 crore <= income < 5 crore"':<63}|'
                      f'{f'{result} x 25% = {perc(result, 25):.2f}':^35}|')
                surcharge = perc(result, 25)
            else:
                print(f'|{'Add: Surcharge (an extra charge, other than tax) at the rate':<63}|{" ":>35}|\n'
                      f'|{'of 37% of basic tax for income greater than equal to 5 crore':<63}|'
                      f'{f'{result} x 37% = {perc(result, 37):.2f}':^35}|')
                surcharge = perc(result, 37)
            print(f"|{' ':>64}{'-':->35}|")
            print(f"|{'Income tax plus surcharge':^63}={(result + surcharge):^35}|")
            print(f'{"":->100}')
            total_tax = (result + surcharge)
        else:
            total_tax = result

        print(f"|{'Add: Health and education cess (at the rate of 4%)':<63}|"
              f"{f'{total_tax} x 4% = {perc(total_tax, 4):.2f}':^35}|")
        tax_payable = (total_tax + perc(total_tax, 4))
        print(f"|{' ':>64}{'-':->35}|")
        print(f"|{'Total income tax payable.':^63}={tax_payable:^35}|")
        print(f'{"":->100}')
        print()
        print(f"So Mr.{name.title()}, as you can see, according to the details provided by you,\n"
              f"your income tax liability for this year is: INR {tax_payable:.2f}.")
        print()
        print(f"Thanks to interact with us, Mr.{name.title()}.\n"
              f"Have a good time.")

else:
    print('Then why are you here idiot.\n'
          'yaha jhunjhuna bajane ke liye aaye ho ka!😂😂😂😂')
input("Got it")
