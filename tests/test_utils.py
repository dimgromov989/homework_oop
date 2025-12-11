import json

from src.utils import create_obj_from_json, read_json


def test_read_json(tmp_path):
    data = [
        {
            "name": "Еда",
            "description": "Продукты",
            "products": [
                {"name": "Банан", "description": "жёлтый", "price": 15.0, "quantity": 3}
            ],
        }
    ]
    json_file = tmp_path / "data.json"
    json_file.write_text(json.dumps(data, ensure_ascii=False), encoding="utf-8")
    result = read_json(json_file)
    assert result == data


def test_create_obj_from_json():
    data = [
        {
            "name": "Бытовая техника",
            "description": "Техника для дома",
            "products": [
                {
                    "name": "Утюг",
                    "description": "Паровой",
                    "price": 2000.0,
                    "quantity": 5,
                }
            ],
        }
    ]

    categories = create_obj_from_json(data)

    assert len(categories) == 1
    cat = categories[0]
    assert cat.name == "Бытовая техника"

    output_lines = cat.list_products.strip().split("\n")
    assert len(output_lines) == 1
    assert "Утюг" in output_lines[0]
    assert "2000.0 руб." in output_lines[0]
    assert "Остаток: 5 шт" in output_lines[0]
