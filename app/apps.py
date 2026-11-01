from django.apps import AppConfig


class AppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app'


def test_gemini_models(request):
    try:
        print("\nAvailable Gemini models:")

        for model in client.models.list():
            if "generateContent" in (model.supported_actions or []):
                print(model.name)

        return JsonResponse({
            "message": "Model list printed in Django terminal."
        })

    except Exception as e:
        print("Model listing error:", str(e))
        return JsonResponse({
            "error": "Unable to retrieve available models."
        }, status=502)