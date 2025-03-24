<?php

namespace Common\Modules\Infrastructure\Helper;

use Common\Modules\Goods\Domain\Repository\GoodsBrandRepository;

class SetListOriginBrandInfo extends SetListOriginRelationInfo
{
    /**
     * @var string 原始信息字段
     */
    protected $originInfoField = 'origin_brand_info';

    /**
     * @var array 原始信息列表主键字段
     */
    protected $originListPrimaryKeyFields = ['brand_id'];

    protected $setFields = [];

    /**
     * @return $this
     */
    public function setDefaultSetFields() {
        $this->addSetField('brand_name', '')
            ->addSetField('brand_num', '');
        return $this;
    }

    /**
     * 设置订单明细默认场景的商品信息
     *
     * @param array $list
     * @param array $brandList
     * @return void
     */
    public function listSet(&$list, $brandList = null, $companyId = null) {
        if ($list && is_null($brandList)) {
            if (is_null($companyId)) {
                $companyId = get_company_id();
            }
            $brandIds = array_column($list, 'brand_id');
            $brandIds = ArrayHelper::idsArrayDeleteValue($brandIds, null, '');
            $brandList  = (new GoodsBrandRepository())->getList($companyId, $brandIds);
        }
        $setListOriginGoodsInfo = new static();
        $setListOriginGoodsInfo->setDefaultSetFields();
        $setListOriginGoodsInfo->setList($list, $brandList);
    }

}