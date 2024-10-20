import json
import requests


def get_twitter_followers():
    """
        Fetches a list of Twitter followers for a specified user and writes their screen names to a JSON file.

        This function sends a request to the Twitter GraphQL API, processes the response,
        and extracts follower screen names, saving them to 'twitterfile.json'.
        """
    cookies = {
        'night_mode': '2',
        'kdt': 'ddFohiZUSqZrFTRSCrVDZOpCaml74pFsQWxxIkLQ',
        'des_opt_in': 'N',
        'dnt': '1',
        'guest_id': 'v1%3A172923927382024758',
        'guest_id_marketing': 'v1%3A172923927382024758',
        'guest_id_ads': 'v1%3A172923927382024758',
        'gt': '1847698396997701856',
        'external_referer': 'padhuUp37zjgzgv1mFWxJ12Ozwit7owX|0|8e8t2xd8A2w%3D',
        'auth_token': 'd44411967ca042b102ed4a0ea9b91d19a420bb06',
        'ct0': '4e41bbf4d447c22f0196aa06e33411bf9e2a5692beff1802e027a120c8a9ac3e13bd9dc953f72c9ffbb564419655c1aa7e7e303498e200391cbb5da090ec5125916ff7c6459ea0f3374ace9dfb8b20e9',
        'att': '1-tDfnZX4jNBncmIstrLgfcDznSgHrrR4iUqH7o22f',
        'lang': 'en',
        'twid': 'u%3D1847167033018060800',
        'personalization_id': '"v1_UVBHR26NknUfFiOJO7oCwg=="',
    }

    headers = {
        'accept': '*/*',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
        'authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA',
        'content-type': 'application/json',
        # 'cookie': 'night_mode=2; kdt=ddFohiZUSqZrFTRSCrVDZOpCaml74pFsQWxxIkLQ; des_opt_in=N; dnt=1;
        # guest_id=v1%3A172923927382024758; guest_id_marketing=v1%3A172923927382024758;
        # guest_id_ads=v1%3A172923927382024758; gt=1847698396997701856;
        # external_referer=padhuUp37zjgzgv1mFWxJ12Ozwit7owX|0|8e8t2xd8A2w%3D;
        # auth_token=d44411967ca042b102ed4a0ea9b91d19a420bb06;
        # ct0=4e41bbf4d447c22f0196aa06e33411bf9e2a5692beff1802e027a120c8a9ac3e13bd9dc953f72c9ffbb564419655c1aa7e7e303498e200391cbb5da090ec5125916ff7c6459ea0f3374ace9dfb8b20e9; att=1-tDfnZX4jNBncmIstrLgfcDznSgHrrR4iUqH7o22f; lang=en; twid=u%3D1847167033018060800; personalization_id="v1_UVBHR26NknUfFiOJO7oCwg=="',
        'priority': 'u=1, i',
        'referer': 'https://x.com/Google/followers',
        'sec-ch-ua': '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 '
                      'Safari/537.36',
        'x-client-transaction-id': 'Wmc0qdHBWFq3y14qxJBow3x6ey/B0Jur4NINfLpeOMqEihRUSGq91/tv4GMvgDk8'
                                   '/gnBnliv2ZBS7h1qmPu6pQVjWWUVWQ',
        'x-client-uuid': 'c0bf0551-9502-4f32-a209-a0198cc6d1c4',
        'x-csrf-token': '4e41bbf4d447c22f0196aa06e33411bf9e2a5692beff1802e027a120c8a9ac3e13bd9dc953f72c9ffbb564419655c1aa7e7e303498e200391cbb5da090ec5125916ff7c6459ea0f3374ace9dfb8b20e9',
        'x-twitter-active-user': 'yes',
        'x-twitter-auth-type': 'OAuth2Session',
        'x-twitter-client-language': 'en',
    }

    params = {
        'variables': '{"userId":"20536157","count":20,"includePromotedContent":false}',
        'features': '{"rweb_tipjar_consumption_enabled":true,"responsive_web_graphql_exclude_directive_enabled":true,'
                    '"verified_phone_label_enabled":true,"creator_subscriptions_tweet_preview_api_enabled":true,'
                    '"responsive_web_graphql_timeline_navigation_enabled":true,'
                    '"responsive_web_graphql_skip_user_profile_image_extensions_enabled":false,'
                    '"communities_web_enable_tweet_community_results_fetch":true,'
                    '"c9s_tweet_anatomy_moderator_badge_enabled":true,"articles_preview_enabled":true,'
                    '"responsive_web_edit_tweet_api_enabled":true,'
                    '"graphql_is_translatable_rweb_tweet_is_translatable_enabled":true,'
                    '"view_counts_everywhere_api_enabled":true,"longform_notetweets_consumption_enabled":true,'
                    '"responsive_web_twitter_article_tweet_consumption_enabled":true,'
                    '"tweet_awards_web_tipping_enabled":false,"creator_subscriptions_quote_tweet_preview_enabled":false,'
                    '"freedom_of_speech_not_reach_fetch_enabled":true,"standardized_nudges_misinfo":true,'
                    '"tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled":true,'
                    '"rweb_video_timestamps_enabled":true,"longform_notetweets_rich_text_read_enabled":true,'
                    '"longform_notetweets_inline_media_enabled":true,"responsive_web_enhance_cards_enabled":false}',
    }

    response = requests.get(
        'https://x.com/i/api/graphql/gwv4MK0diCpAJ79u7op1Lg/Followers',
        params=params,
        cookies=cookies,
        headers=headers,
    )

    out_file = open('twitterfile.json', 'w')
    jd = response.json()
    try:
        blocks = jd.get('data').get('user').get('result').get('timeline').get('timeline').get('instructions')[3].get(
            'entries')

        for block in blocks:
            if block:
                name = block.get('content').get('itemContent').get('user_results').get('result').get('legacy').get(
                    'screen_name')
                out_file.write(json.dumps(dict(Followers=name)) + '\n')
    except Exception as e:
        print(str(e))

# Call the function to execute
get_twitter_followers()
