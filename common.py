import os

class Config:
    log_dir = './log/log.txt'
    video_dir = "F:\\白百何\\interview\\interview-1.mp4"

    face_detection_model = 'model/face_detector.resnet50_retinanet.inference.h5'
    landmark_predictor = "D:\\CSLT\\Retinanet_face\\keras-retinanet\\model\\dlib\\shape_predictor_68_face_landmarks.dat"
    face_validation_path = "D:\\CSLT\\Retinanet_face\\keras-retinanet\\facenet_code\\20180402-114759"

    image_files = ["./images/白百何/白百何1.jpg","./images/白百何/白百何2.jpg",
                   "./images/白百何/白百何3.jpg","./images/白百何/白百何4.jpg"]

    lip_movement_modelpath = "D:\\CSLT\\Retinanet_face\\keras-retinanet\\model\\lip_movement_model\\2_64_False_True_0.5_lip_motion_net_model.h5"
    syncnet_model = "D:\\CSLT\\Retinanet_face\\keras-retinanet\\syncnet\\data\\syncnet_v2.model"
    exp_name = os.path.basename(log_dir)

    # visual
    # debug = True
    showimg = True
    # Tracker
    tracker_type = 'MOSSE'
    patience = 8
    # face validation

    validation_imagesize = 160
    margin = 44
    threshold = 0.9


    # speaker validation
    starting_confidence = 4
    patient_confidence = 3
    @property
    def input_shape(self):
        return (self.minibatch_size, self.nr_channel) + self.image_shape

config = Config()