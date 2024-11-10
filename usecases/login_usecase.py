from models import User
import cv2
import mediapipe as mp
from deepface import DeepFace
import numpy as np
import base64

mp_drawing = mp.solutions.drawing_utils
mp_face_detection = mp.solutions.face_detection

class LoginUseCase:
    def face_recognition(self, stored_photo_path, face_image):
        # Decodificar a imagem base64
        header, encoded = face_image.split(',', 1)
        data = base64.b64decode(encoded)

        # Converter a imagem em um formato que o OpenCV pode usar
        nparr = np.frombuffer(data, np.uint8)
        uploaded_image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

        # Inicializar o detector de rostos do mediapipe
        face_detection = mp_face_detection.FaceDetection(model_selection=1, min_detection_confidence=0.5)
        results = face_detection.process(cv2.cvtColor(uploaded_image, cv2.COLOR_BGR2RGB))

        landmarks = []  # Lista para armazenar os landmarks

        if results.detections:
            for detection in results.detections:
                # Recortar o rosto detectado
                bounding_box = detection.location_data.relative_bounding_box
                height, width, _ = uploaded_image.shape
                x = int(bounding_box.xmin * width)
                y = int(bounding_box.ymin * height)
                w = int(bounding_box.width * width)
                h = int(bounding_box.height * height)
                face_image_cropped = uploaded_image[y:y + h, x:x + w]

                # Desenhar o retângulo em volta do rosto detectado
                cv2.rectangle(uploaded_image, (x, y), (x + w, y + h), (0, 255, 0), 2)

                # Adicionar landmarks à lista
                landmarks.append({
                    'x': bounding_box.xmin,
                    'y': bounding_box.ymin,
                    'width': bounding_box.width,
                    'height': bounding_box.height
                })

                # Verificar se a imagem do rosto corresponde à foto armazenada
                result = DeepFace.verify(face_image_cropped, stored_photo_path)
                if result['verified']:
                    return True, landmarks  # Retorna também os landmarks
        print(f'Landmarks (nenhum rosto detectado): {landmarks}')
        return False, landmarks  # Retorna os landmarks mesmo que a verificação falhe