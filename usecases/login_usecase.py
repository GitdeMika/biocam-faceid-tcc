from models import User
import cv2
import mediapipe as mp
from deepface import DeepFace
import numpy as np
import base64
from PIL import Image
import io

mp_drawing = mp.solutions.drawing_utils
mp_face_detection = mp.solutions.face_detection


class LoginUseCase:
    def face_recognition(self, stored_photo_path, face_image):
        try:
            # Decodificar a imagem base64
            header, encoded = face_image.split(',', 1)
            data = base64.b64decode(encoded)

            # Converter a imagem em um formato que o OpenCV pode usar
            nparr = np.frombuffer(data, np.uint8)
            uploaded_image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

            if uploaded_image is None:
                print("Erro ao decodificar a imagem")
                return False, []

            # Redimensionar a imagem se for muito grande
            max_dimension = 1024
            height, width = uploaded_image.shape[:2]
            if max(height, width) > max_dimension:
                scale = max_dimension / max(height, width)
                uploaded_image = cv2.resize(uploaded_image,
                                            (int(width * scale), int(height * scale)))

            # Inicializar o detector de rostos do mediapipe
            with mp_face_detection.FaceDetection(
                    model_selection=1,
                    min_detection_confidence=0.5) as face_detection:

                results = face_detection.process(cv2.cvtColor(uploaded_image, cv2.COLOR_BGR2RGB))

            landmarks = []

            if results.detections:
                for detection in results.detections:
                    # Recortar o rosto detectado
                    bounding_box = detection.location_data.relative_bounding_box
                    height, width, _ = uploaded_image.shape
                    x = int(bounding_box.xmin * width)
                    y = int(bounding_box.ymin * height)
                    w = int(bounding_box.width * width)
                    h = int(bounding_box.height * height)

                    # Garantir que as coordenadas estão dentro dos limites da imagem
                    x = max(0, x)
                    y = max(0, y)
                    w = min(w, width - x)
                    h = min(h, height - y)

                    face_image_cropped = uploaded_image[y:y + h, x:x + w]

                    # Verificar se o recorte foi bem sucedido
                    if face_image_cropped.size == 0:
                        print("Erro ao recortar o rosto")
                        continue

                    landmarks.append({
                        'x': bounding_box.xmin,
                        'y': bounding_box.ymin,
                        'width': bounding_box.width,
                        'height': bounding_box.height
                    })

                    try:
                        result = DeepFace.verify(face_image_cropped, stored_photo_path)
                        if result['verified']:
                            return True, landmarks
                    except Exception as e:
                        print(f"Erro na verificação facial: {str(e)}")
                        continue

            print(f'Landmarks (nenhum rosto detectado ou verificação falhou): {landmarks}')
            return False, landmarks

        except Exception as e:
            print(f"Erro no processamento da imagem: {str(e)}")
            return False, []