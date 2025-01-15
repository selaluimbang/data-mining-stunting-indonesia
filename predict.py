import pandas as pd
from model import StuntingModel

def make_prediction(data):
    model = StuntingModel()

    model.load_model('7_xgb_default_3_0_82.pkl')
    # print("----")
    # print(model.print_model())
    # print("----")

    # print("----")
    # print(model.print_features())
    # print("----")

    # print("----")
    # print(data)
    # print("----")

    # print("----")
    # print("Model expects:", model.print_features())
    # print("Input features:", data.columns)
    # print("----")

    # data = pd.get_dummies(data, columns=['persentase_akses_air_minum_layak', 'indeks_pembangunan_literasi', 'indeks_pembangunan_manusia',
    #                                      'penerima_bpjs_non_pbi', 'prevalensi_underweight', 'prevalensi_wasting'], drop_first=True)

    # if 'persentase_akses_air_minum_layak' not in data.columns:
    #     data['persentase_akses_air_minum_layak'] = 0.0

    # if 'indeks_pembangunan_literasi' not in data.columns:
    #     data['indeks_pembangunan_literasi'] = 0.0

    # if 'indeks_pembangunan_manusia' not in data.columns:
    #     data['indeks_pembangunan_manusia'] = 0.0
    
    # if 'penerima_bpjs_non_pbi' not in data.columns:
    #     data['penerima_bpjs_non_pbi'] = 0.0

    # if 'prevalensi_underweight' not in data.columns:
    #     data['prevalensi_underweight'] = 0.0

    # if 'prevalensi_wasting' not in data.columns:
    #     data['prevalensi_wasting'] = 0.0
    
    prediction = model.predict(data)
    # prediction = [1]
    print("----")
    print(f"RESULT : {prediction}")
    print("----")
    return f"Daerah Prioritas" if prediction[0] == 1 else f"Bukan Daerah Prioritas"
