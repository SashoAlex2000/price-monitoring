from concrete_classes.technopolis.techopolis_item_category import TechnopolisMainItemCategory, \
    TechnopolisSubItemCategory


def export_categories_for_crawl() -> list[TechnopolisSubItemCategory]:

    """
    Export a list of `TechnopolisSubItemCategory` pre-configured instances to be crawled
    """

    # TODO think about some more efficient way

    categories_to_crawl: list[TechnopolisSubItemCategory] = []

    # TV
    _tv_main_cateogry: TechnopolisMainItemCategory = TechnopolisMainItemCategory(
        category_name='TV--Video-i-Gaming',
        category_number='P1109',
    )
    __tv_subcategory: TechnopolisSubItemCategory = TechnopolisSubItemCategory(
        category_name='Televizori',
        category_number='P11090104',
        parent=_tv_main_cateogry
    )
    categories_to_crawl.append(__tv_subcategory)
    __soundbar_subcategory: TechnopolisSubItemCategory = TechnopolisSubItemCategory(
        category_name='Soundbar-sistemi',
        category_number='P11090503',
        parent=_tv_main_cateogry
    )
    categories_to_crawl.append(__soundbar_subcategory)
    __bluray_dvd__subcategory: TechnopolisSubItemCategory = TechnopolisSubItemCategory(
        category_name='Blu-Ray-i-DVD-pleari',
        category_number='P11090301',
        parent=_tv_main_cateogry,
    )
    categories_to_crawl.append(__bluray_dvd__subcategory)

    return categories_to_crawl
