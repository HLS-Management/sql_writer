import pytest
from ..source import basic


class Test_Select:
    def test_select_all(self):
        assert basic.select("table") == "SELECT * FROM table"

    def test_select_specific(self):
        assert basic.select("table", ["col1, col2"]) == "SELECT col1, col2 FROM table"

    def test_select_where(self):
        assert basic.select("table", query_fields=["col1", "col2"]) == "SELECT * FROM table WHERE col1 = %s AND col2 = %s"

    @pytest.mark.parametrize("invalid_tables", [
        "",
        ["Bob"],
        {"Never odd or even"},
        ("Do geese see God?",)
        ])
    def test_select_table_type(self, invalid_tables):
        with pytest.raises(Exception):
            basic.select(invalid_tables)

    @pytest.mark.parametrize("invalid_fields", [
        "",
        "test",
        {"Never odd or even"},
        ("Do geese see God?",),
        [1, ["wow"]]
        ])
    def test_select_field_type(self, invalid_fields):
        with pytest.raises(Exception):
            basic.select("test", invalid_fields)

    @pytest.mark.parametrize("invalid_fields", [
        "",
        "test",
        {"Never odd or even"},
        ("Do geese see God?",),
        [1, ["wow"]]
        ])
    def test_select_where_field_type(self, invalid_fields):
        with pytest.raises(Exception):
            basic.select("test", query_fields=invalid_fields)
