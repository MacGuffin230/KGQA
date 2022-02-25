from model import question_classify_model
from model import question_template


class QuestionService:
    """
    问答核心类，接收自然问句，构造查询语句，输出答案
    """

    def __init__(self):
        self.classify_model = question_classify_model.QuestionClassify()
        self.question_template = question_template.QuestionTemplate()

    def get_answer(self, question):
        # 通过分类器获取分类
        question_category = self.classify_model.predict(question)
        # 根据分类获取模板，查询得到答案
        try:
            answer = self.question_template.get_question_answer(question, question_category)
        except BaseException as e:
            answer = "我也还不知道呢"

        return answer


question_service_instance = QuestionService()
