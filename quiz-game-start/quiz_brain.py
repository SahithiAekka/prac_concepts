class QuizBrain:
    
    def __init__(self, q_list):
        self.question_number = 0 
        self.question_list = q_list
        self.score=0
    
    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def get_score(self):
        print(f"Your score is {self.score}")
           
    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1 
            print("That's right!")
        else:
            print("That's wrong!")
            
        print(f"The correct answer is {correct_answer}")
        self.get_score()
    
    
    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        for i in range(0,2):
            print(f"\n****You have two attempts to answer the question {self.question_number}**** \nThis is your attempt no. {i+1}  ")
            user_answer= input(f"Q.{self.question_number}: {current_question.text} (True/False): ")
            if user_answer.lower() == "true" or user_answer.lower() == "false":
                correct_answer=current_question.answer
                self.check_answer(user_answer,correct_answer)
                break
            else: 
                print("Only use true or false")
                if i ==1:
                    print("******This was your last attempt. You can answer the next question******")
                    self.get_score()
            # assert user_answer.lower() == "true" or user_answer.lower() == "false", "Only use true or false"
        
        
    
   
       
          
        
        
        
         
        
        
        
        