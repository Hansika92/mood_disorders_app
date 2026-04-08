def diagnose(depression_score, mania_score):

    if depression_score >= 20:
        severity = "Severe Depression"
    elif depression_score >= 15:
        severity = "Moderately Severe Depression"
    elif depression_score >= 10:
        severity = "Moderate Depression"
    elif depression_score >= 5:
        severity = "Mild Depression"
    else:
        severity = "Minimal Depression"

    if depression_score >= 10 and mania_score < 8:
        return "Major Depressive Disorder", severity

    elif mania_score >= 12 and depression_score < 10:
        return "Mania / Hypomania", severity

    elif mania_score >= 10 and depression_score >= 10:
        return "Bipolar Disorder", severity

    elif depression_score >= 5 and depression_score <= 9:
        return "Dysthymia", severity

    else:
        return "Cyclothymia", severity


