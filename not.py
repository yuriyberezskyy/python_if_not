statement_one = False

statement_two = True


def graduation_reqs(gpa, credits):
    if (gpa >= 2.0) and (credits >= 120):
        return "You meet the requirements to graduate!"
    elif (gpa >= 2.0) and not(credits >= 120):
        return "You do not have enough credits to graduate."
    elif not(gpa >= 2.0) and (credits >= 120):
        return "Your GPA is not high enough to graduate."
    else:
        return "You do not meet either requirement to graduate!"


print(graduation_reqs(1.0, 130))
