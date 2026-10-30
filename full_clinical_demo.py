"""
Comprehensive demonstration of the Clinical Medicine & Health Informatics Toolkit.
"""
from medkit.calculators import calculate_cha2ds2_vasc, calculate_news2, calculate_curb65
from medkit.assessment import MedicalExamEvaluator

def main():
    print("=== CLINICAL MEDICINE TOOLKIT DEMO ===")
    
    # 1. Stroke Risk Stratification
    res = calculate_cha2ds2_vasc(
        age=71,
        sex="female",
        hypertension=True,
        stroke_tia_thromboembolism=True
    )
    print(f"\n[1] CHA2DS2-VASc Evaluation:")
    print(f"  Score: {res['score']}")
    print(f"  Stroke Risk: {res['stroke_risk_percent']}% per year")
    print(f"  Recommendation: {res['recommendation']}")

    # 2. Acute Deterioration (NEWS2)
    news = calculate_news2(
        respiratory_rate=22,
        oxygen_saturation=94,
        on_supplemental_oxygen=False,
        systolic_bp=105,
        heart_rate=98,
        consciousness="Alert",
        temperature=37.8
    )
    print(f"\n[2] NEWS2 Early Warning Score:")
    print(f"  Score: {news['score']}")
    print(f"  Risk Category: {news['risk_category']}")
    print(f"  Action: {news['clinical_response']}")

    # 3. Medical Examination Evaluator
    evaluator = MedicalExamEvaluator()
    evaluator.score_mcq(
        question_id=1,
        stem_answers=[True, False, True, None, False],
        correct_answers=[True, True, True, False, False],
        rationales=[
            "Stem A is standard 1st line.",
            "Stem B is contraindicated.",
            "Stem C is an established association.",
            "Stem D omitted by candidate.",
            "Stem E has no proven benefit."
        ]
    )
    evaluator.score_sba(
        question_id=2,
        user_choice="C",
        correct_choice="C",
        explanation="C is the gold standard diagnostic test."
    )
    report = evaluator.get_summary_report()
    print(f"\n[3] Assessment Summary:")
    print(f"  Total Score: {report['total_obtained']}/{report['total_possible']} ({report['final_percentage']}%)")

if __name__ == "__main__":
    main()
