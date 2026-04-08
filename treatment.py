def treatment_plan(diagnosis, severity):

    if diagnosis == "Major Depressive Disorder":
        if severity in ["Moderate Depression", "Moderately Severe Depression", "Severe Depression"]:
            return "Cognitive Behavioral Therapy (CBT), Antidepressants (SSRIs), Lifestyle modification, Regular follow-up"
        else:
            return "Psychotherapy, Lifestyle changes, Exercise, Sleep hygiene"

    elif diagnosis == "Bipolar Disorder":
        return "Mood stabilizers (Lithium/Valproate), Psychotherapy, Sleep regulation, Regular psychiatric evaluation"

    elif diagnosis == "Mania / Hypomania":
        return "Mood stabilizers, Antipsychotics, Hospitalization if severe"

    elif diagnosis == "Dysthymia":
        return "Psychotherapy, Antidepressants, Lifestyle modification"

    elif diagnosis == "Cyclothymia":
        return "Mood monitoring, Counseling, Mood stabilizers if needed"

    else:
        return "Further psychological evaluation required"

