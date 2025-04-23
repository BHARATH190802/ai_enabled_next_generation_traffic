from django.apps import AppConfig
import torch





class PredictConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "predict"

    def ready(self):
        print("The Model is Loading......")
        path_hubconfig = "yolov5"
        path_weightfile = "predict//best.pt"  # or any custom trained model

        model = torch.hub.load(
            path_hubconfig, "custom", path=path_weightfile, source="local"
        )

        return model