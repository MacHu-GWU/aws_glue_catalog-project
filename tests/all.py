# -*- coding: utf-8 -*-

if __name__ == "__main__":
    from aws_glue_catalog.tests import run_cov_test

    run_cov_test(__file__, "aws_glue_catalog", is_folder=True, preview=False)
