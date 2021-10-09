def grade_score(score):
    if score >= 80:
        return 'A'
    elif score >=75:
        return 'A-'
    elif score >= 70:
        return 'B+'
    elif score >= 65:
        return 'B'
    elif score >= 60:
        return 'B-'
    elif score >= 55:
        return 'C+'
    elif score >= 50:
        return 'C'
    elif score >= 45:
        return 'C'
    elif score >= 40:
        return 'C-'
    elif score >= 35:
        return 'D+'
    else: return 'fail'    