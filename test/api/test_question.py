from base import TestBase


class TestQuestion(TestBase):
    def test_add_question(self):
        add_question ='''{
            "images": "http://p0.ifengimg.com/haina/2016_51/c22b0f030c302ee_w599_h344.jpg",
            "text": "this is xxx"
        }'''
        response = self.fetch('/question/add/', method='POST', body=add_question)
        self.assertEqual(response.code, 200)

    def test_question_nearly(self):
        response = self.fetch('/question/nearly/')
        self.assertEqual(response.code, 200)
        question_object = {}
        if len(response.data['data']) > 0:
            question_object = response.data['data'][0]
        self.__test_question(question_object)

    def __test_question(self, question_object):
        response = self.fetch('/question/%s'%(question_object['id']))
        self.assertEqual(response.code, 200)

        question_object = response.data['data']
        self.__test_add_answer(question_object)
        self.__test_agree(question_object)

    def __test_add_answer(self, question_object):
        add_answer = '''{
            "images": "http://p0.ifengimg.com/haina/2016_51/c22b0f030c302ee_w599_h344.jpg",
            "text": "this is xxx"
        }'''
        response = self.fetch('/question/%s/answer/add/'%(question_object['id']), method='POST', body=add_answer)
        self.assertEqual(response.code, 200)

    def __test_agree(self, question_object):
        response = self.fetch('/answer/%s/agree/'%(question_object['answers'][0]['id']), method='POST', body="{}")
        self.assertEqual(response.code, 200)
