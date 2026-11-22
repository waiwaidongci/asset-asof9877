"""桂桥社区交接簿，含期初结转、跨月借还、退役和重复上传。"""


_EVENTS = (
    ("GQ-01", "充电电钻", "2026-08-28", 1, "accept"),
    ("GQ-02", "数字万用表", "2026-08-31", 1, "accept"),
    ("GQ-03", "园艺修枝剪", "2026-09-03", 1, "accept"),
    ("GQ-01", None, "2026-09-12", 1, "check-out"),
    ("GQ-02", None, "2026-09-30", 1, "check-out"),
    ("GQ-02", None, "2026-09-30", 2, "check-in"),
    ("GQ-01", None, "2026-10-01", 1, "check-in"),
    ("GQ-04", "手持砂光机", "2026-10-02", 1, "accept"),
    ("GQ-02", None, "2026-10-31", 1, "retire"),
    ("GQ-03", None, "2026-10-31", 1, "check-out"),
    ("GQ-05", "折叠踏梯", "2026-11-01", 1, "accept"),
    ("GQ-04", None, "2026-11-15", 1, "check-out"),
    ("GQ-01", None, "2026-11-20", 1, "check-out"),
    ("GQ-03", None, "2026-11-20", 1, "check-in"),
    ("GQ-01", None, "2026-11-21", 1, "check-in"),
    ("GQ-06", "棘轮扳手套装", "2026-11-21", 1, "accept"),
)


def demo_rows() -> list[dict]:
    rows = [
        {"event_id": f"GQ-E{index:03d}", "asset_id": asset_id, "asset_name": asset_name,
         "event_date": day, "sequence": sequence, "event_type": event_type}
        for index, (asset_id, asset_name, day, sequence, event_type) in enumerate(_EVENTS, 1)
    ]
    rows.append(rows[9].copy())
    return rows
