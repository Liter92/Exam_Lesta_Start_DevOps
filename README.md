﻿
Для запуска проекта локально

 1. Небоходимо клонировать его с github командой:

    git clone git@github.com:Liter92/Exam_Lesta_Start_DevOps.git

    ![alt text](/attachments/image.png)
 
 2. Сбилдить образ Flask Приложения комндой:
    docker build -t task_examen_web .

    ![alt text](/attachments/image1.png)
 
 3. Выполнить комнду:
    docker-compose up -d

    ![alt text](/attachments/image2.png)


 4. Проект готов к использования на локальной машине:

    ![alt text](/attachments/image5.png)

    ![alt text](/attachments/image3.png)

    ![alt text](/attachments/image4.png)


Как настроить Jenkins, Как работает CI/CD

   В каталоге jenkins находяться два пайплайна для тестирования и развертывания приложения на указанных агентах. При успешном выполнении первого пайплайна автоматический начинается выполение второго. Производиться тестрирование валидности Flask кода а так же возвращемый ответ от /ping эндпоинта.


   ![alt text](/attachments/image6.png)

   ![alt text](/attachments/image7.png)

   ![alt text](/attachments/image9.png)

   ![alt text](/attachments/image10.png)

 
Примеры API-запросов

   ![alt text](/attachments/image8.png)
 
 
Ендпоинт в формате <IP-VM>:<PORT>/results

   curl -X POST http://37.9.53.134:5000/submit -H "Content-Type: application/json" -d '{"name": "Roman", "score": 100}'

   curl http://37.9.53.134:5000/results

   curl http://37.9.53.134:5000/ping
