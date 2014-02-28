#!/usr/bini/env python 
import json
import requests

url  ="http://www.myntra.com/searchws/search/styleids2"


jsonline = {"query":"(global_attr_article_type_facet:(\"Sports Shoes\") AND global_attr_gender:(\"Men\")) AND (count_options_availbale:[1 TO *])","start":24,"rows":50,"sort":[{"sort_field":"count_options_availbale","order_by":"desc"},{"sort_field":"style_store4_sort_field","order_by":"desc"},{"sort_field":"potential_revenue_sort_field","order_by":"desc"},{"sort_field":"global_attr_catalog_add_date","order_by":"desc"}],"return_docs":True,"facetField":["Sport_article_attr","Upper_Material_article_attr","Fastening_article_attr","Outsole_article_attr","Cleats_article_attr","Width_article_attr"],"colour_grouping":True,"fq":[],"facet":False,"mongoData":{"trafficData":{"source":"referral","medium":"google.co.in","campaign":None,"channel":"Organic"},"referer":{"host":"www.myntra.com","path":"/shop/men-footwear","query":"hpbnr=mm-newui-sub-mens-footwear-24sep","domain":"myntra.com"},"deviceData":{"isMobile":False},"mabTestData":{"mabtests":[{"abtestName":"productui","variantName":"newui","filteredOut":"False"},{"abtestName":"telesales","variantName":"shownumber","filteredOut":"False"},{"abtestName":"splash","variantName":"control","filteredOut":"False"},{"abtestName":"loginbox","variantName":"v3","filteredOut":"False"},{"abtestName":"boostedSearch","variantName":"control","filteredOut":"False"},{"abtestName":"newVsOld","variantName":"new","filteredOut":"False","userType":"new"},{"abtestName":"SocialShare","variantName":"control","filteredOut":"False"},{"abtestName":"LoginSplash","variantName":"control","filteredOut":"False"},{"abtestName":"ColourSelect","variantName":"test","filteredOut":"False"},{"abtestName":"NewLayout","variantName":"test","filteredOut":"False"},{"abtestName":"stickySize","variantName":"control","filteredOut":"False"},{"abtestName":"secureSignin","variantName":"secure","filteredOut":"False"},{"abtestName":"newSignupAB","variantName":"control","filteredOut":"False"},{"abtestName":"checkout","variantName":"test","filteredOut":"False"},{"abtestName":"couponAutoApplyTest","variantName":"control","filteredOut":"False"},{"abtestName":"SearchOptim","variantName":"test","filteredOut":"False"},{"abtestName":"loginSignupABTest","variantName":"test","filteredOut":"False"},{"abtestName":"WebEngageFeedback","variantName":"control","filteredOut":"False"},{"abtestName":"WebEngageNotifications","variantName":"test","filteredOut":"False"},{"abtestName":"LocationBreadcrumbABTest","variantName":"test","filteredOut":"False"},{"abtestName":"styleRevenueAdjusted6","variantName":"test4","filteredOut":"False"},{"abtestName":"nudge","variantName":"control","filteredOut":"False"},{"abtestName":"nudgeShow","variantName":"test","filteredOut":"False"},{"abtestName":"regV2","variantName":"test","filteredOut":"False"},{"abtestName":"regV2PhoneRequired","variantName":"control","filteredOut":"False"},{"abtestName":"njswHP","variantName":"control","filteredOut":"False"},{"abtestName":"idptest","variantName":"test","filteredOut":"False"},{"abtestName":"checkout_flow_java","variantName":"java","filteredOut":"False"},{"abtestName":"coupon_applicability","variantName":"cart","filteredOut":"False"},{"abtestName":"promo_coupons","variantName":"validate","filteredOut":"False"},{"abtestName":"quickLookOffer","variantName":"test","filteredOut":"False"},{"abtestName":"promo_coupons_mobile","variantName":"validate","filteredOut":"False"}]}}}




def main3(val):
    for key2, val2 in val.items():
        print "="*20
        print key2, ":", val2
        print "*"*20
        main2(key2, val2)


def main2(key, val):
    key = str(key)

    if type(val) is dict:
        main3(val)

    elif  type(val) is list:
        for subval in val:
            if (type(subval) is dict) or (type(subval) is tuple):
                main3(subval)
            else:
                #print "%s : %s" %(key, subval)
                pass
    else:
        print "%s : %s" %(key, val)
         
         
       

    

def main():
    for key, val in jsonline.items():
        main2(key, val)



  
if __name__=="__main__":
    main()
