# Copyright (c) Facebook, Inc. and its affiliates. All Rights Reserved.
"""Centralized catalog of paths."""


class DatasetCatalog:
    DATASETS = {
        # ------------------------------------------------------------------
        # 3D-FRONT Images
        # ------------------------------------------------------------------
        "Front3DImages_Train": {
            "file_list_path": "resources/front3d/train_list_2d.txt",
            "dataset_root_path": "data/front3d/",
            "factory": "Front3D"
        },

        "Front3DImages_Validation": {
            "file_list_path": "resources/front3d/validation_list_2d.txt",
            "dataset_root_path": "data/front3d/",
            "factory": "Front3D"
        },

        "Front3DImages_Test": {
            "file_list_path": "resources/front3d/test_list_2d.txt",
            "dataset_root_path": "data/front3d/",
            "factory": "Front3D"
        },

        # ------------------------------------------------------------------
        # 3D-FRONT
        # ------------------------------------------------------------------
        "Front3D_Sample": {
            "file_list_path": "resources/front3d/sample.txt",
            "dataset_root_path": "data/front3d-sample/",
            "factory": "Front3D"
        },

        "Front3D_Train": {
            "file_list_path": "resources/front3d/train_list_3d.txt",
            "dataset_root_path": "data/front3d/",
            "factory": "Front3D"
        },

        "Front3D_Validation": {
            "file_list_path": "resources/front3d/validation_list_3d.txt",
            "dataset_root_path": "data/front3d/",
            "factory": "Front3D"

        },

        "Front3D_Test": {
            "file_list_path": "resources/front3d/test_list_3d.txt",
            "dataset_root_path": "data/front3d/",
            "factory": "Front3D"
        }
    }

    @staticmethod
    def get(name):
        attrs = DatasetCatalog.DATASETS[name]
        return attrs
