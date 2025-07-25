"""
🧠 AI Engine for DoganBS v1.2
Advanced AI capabilities and machine learning features
💙 In Memory of Omar (2007-2024)
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import json
import random
from typing import List, Dict, Any, Optional
import warnings
warnings.filterwarnings('ignore')

# ML imports with fallbacks
try:
    from sklearn.ensemble import IsolationForest, RandomForestRegressor
    from sklearn.preprocessing import StandardScaler, MinMaxScaler
    from sklearn.linear_model import LinearRegression, Ridge
    from sklearn.cluster import KMeans
    from sklearn.metrics import mean_absolute_error, r2_score
    from sklearn.model_selection import train_test_split
    ML_AVAILABLE = True
except ImportError:
    ML_AVAILABLE = False

try:
    from prophet import Prophet
    PROPHET_AVAILABLE = True
except ImportError:
    PROPHET_AVAILABLE = False

class AIEngine:
    """Advanced AI Engine for Business Intelligence"""

    def __init__(self):
        self.models = {}
        self.scalers = {}
        self.insights_cache = {}
        self.anomaly_threshold = 2.0

    def generate_smart_insights(self, data: pd.DataFrame, kpi: str) -> List[Dict]:
        """Generate AI-powered business insights"""
        insights = []

        if kpi not in data.columns:
            return insights

        values = data[kpi].dropna()
        if len(values) < 3:
            return insights

        # Trend analysis
        trend = self._analyze_trend(values)
        insights.append({
            'type': 'trend',
            'title': f'{kpi} Trend Analysis',
            'insight': f'{kpi} shows {trend["direction"]} trend with {trend["strength"]} strength',
            'confidence': trend['confidence'],
            'action': self._get_trend_action(trend, kpi)
        })

        # Volatility analysis
        volatility = self._analyze_volatility(values)
        if volatility['level'] == 'high':
            insights.append({
                'type': 'volatility',
                'title': f'{kpi} Volatility Alert',
                'insight': f'High volatility detected in {kpi} (σ={volatility["std"]:.2f})',
                'confidence': 0.85,
                'action': f'Consider stabilizing factors affecting {kpi}'
            })

        # Performance vs benchmark
        benchmark = self._get_benchmark(kpi)
        if benchmark:
            performance = self._compare_to_benchmark(values.iloc[-1], benchmark)
            insights.append({
                'type': 'benchmark',
                'title': f'{kpi} Benchmark Comparison',
                'insight': f'{kpi} is {performance["status"]} benchmark by {performance["difference"]:.1f}%',
                'confidence': 0.90,
                'action': performance['recommendation']
            })

        return insights

    def predict_kpi(self, data: pd.DataFrame, kpi: str, periods: int = 6, method: str = 'auto') -> Dict:
        """Advanced KPI prediction with multiple models"""
        if kpi not in data.columns:
            return {'error': f'KPI {kpi} not found in data'}

        values = data[kpi].dropna()
        if len(values) < 10:
            return {'error': 'Insufficient data for prediction'}

        predictions = {}

        # Linear Regression
        if ML_AVAILABLE:
            linear_pred = self._linear_prediction(values, periods)
            predictions['linear'] = linear_pred

        # Prophet (if available)
        if PROPHET_AVAILABLE and 'Date' in data.columns:
            prophet_pred = self._prophet_prediction(data, kpi, periods)
            predictions['prophet'] = prophet_pred

        # ARIMA-like simple prediction
        arima_pred = self._simple_arima_prediction(values, periods)
        predictions['arima'] = arima_pred

        # Ensemble prediction
        ensemble_pred = self._ensemble_prediction(predictions, periods)

        return {
            'predictions': ensemble_pred,
            'confidence_intervals': self._calculate_confidence_intervals(predictions, periods),
            'model_performance': self._evaluate_models(predictions, values),
            'recommendations': self._generate_prediction_recommendations(ensemble_pred, values)
        }

    def detect_anomalies(self, data: pd.DataFrame, kpi: str, method: str = 'isolation_forest') -> Dict:
        """Advanced anomaly detection"""
        if kpi not in data.columns:
            return {'error': f'KPI {kpi} not found in data'}

        values = data[kpi].dropna()
        if len(values) < 10:
            return {'error': 'Insufficient data for anomaly detection'}

        anomalies = {}

        if ML_AVAILABLE and method == 'isolation_forest':
            anomalies['isolation_forest'] = self._isolation_forest_anomalies(values)

        # Statistical anomalies (Z-score)
        anomalies['statistical'] = self._statistical_anomalies(values)

        # Seasonal anomalies
        if len(values) >= 12:
            anomalies['seasonal'] = self._seasonal_anomalies(values)

        # Combine results
        combined_anomalies = self._combine_anomaly_results(anomalies, values)

        return {
            'anomalies': combined_anomalies,
            'severity': self._assess_anomaly_severity(combined_anomalies, values),
            'explanations': self._explain_anomalies(combined_anomalies, values),
            'recommendations': self._anomaly_recommendations(combined_anomalies)
        }

    def smart_threshold_optimization(self, data: pd.DataFrame, kpi: str, target: float) -> Dict:
        """AI-powered threshold optimization"""
        if kpi not in data.columns:
            return {'error': f'KPI {kpi} not found in data'}

        values = data[kpi].dropna()
        if len(values) < 20:
            return {'error': 'Insufficient data for threshold optimization'}

        # Analyze historical performance
        performance_analysis = self._analyze_performance_distribution(values, target)

        # Optimize thresholds based on data distribution
        optimized_thresholds = self._optimize_thresholds(values, target)

        # Calculate threshold effectiveness
        effectiveness = self._calculate_threshold_effectiveness(values, optimized_thresholds)

        return {
            'optimized_thresholds': optimized_thresholds,
            'performance_analysis': performance_analysis,
            'effectiveness_score': effectiveness,
            'recommendations': self._threshold_recommendations(optimized_thresholds, performance_analysis)
        }

    def correlation_analysis(self, data: pd.DataFrame) -> Dict:
        """Advanced correlation and causation analysis"""
        numeric_cols = data.select_dtypes(include=[np.number]).columns.tolist()

        if len(numeric_cols) < 2:
            return {'error': 'Insufficient numeric columns for correlation analysis'}

        # Correlation matrix
        corr_matrix = data[numeric_cols].corr()

        # Find strong correlations
        strong_correlations = self._find_strong_correlations(corr_matrix)

        # Lag correlation analysis
        lag_correlations = self._lag_correlation_analysis(data, numeric_cols)

        # Causation hints (Granger-like)
        causation_hints = self._analyze_causation_hints(data, numeric_cols)

        return {
            'correlation_matrix': corr_matrix.to_dict(),
            'strong_correlations': strong_correlations,
            'lag_correlations': lag_correlations,
            'causation_hints': causation_hints,
            'insights': self._generate_correlation_insights(strong_correlations, lag_correlations)
        }

    def smart_segmentation(self, data: pd.DataFrame, features: List[str], n_segments: int = 5) -> Dict:
        """AI-powered customer/data segmentation"""
        if not ML_AVAILABLE:
            return {'error': 'ML libraries not available for segmentation'}

        # Prepare data
        segment_data = data[features].dropna()
        if len(segment_data) < n_segments * 2:
            return {'error': 'Insufficient data for segmentation'}

        # Normalize data
        scaler = StandardScaler()
        normalized_data = scaler.fit_transform(segment_data)

        # K-means clustering
        kmeans = KMeans(n_clusters=n_segments, random_state=42)
        segments = kmeans.fit_predict(normalized_data)

        # Analyze segments
        segment_analysis = self._analyze_segments(segment_data, segments, features)

        # Generate segment insights
        segment_insights = self._generate_segment_insights(segment_analysis)

        return {
            'segments': segments.tolist(),
            'segment_centers': kmeans.cluster_centers_.tolist(),
            'segment_analysis': segment_analysis,
            'insights': segment_insights,
            'recommendations': self._segment_recommendations(segment_analysis)
        }

    def predictive_maintenance(self, data: pd.DataFrame, asset_col: str, performance_cols: List[str]) -> Dict:
        """Predictive maintenance analysis"""
        if asset_col not in data.columns:
            return {'error': f'Asset column {asset_col} not found'}

        maintenance_insights = {}

        for asset in data[asset_col].unique():
            asset_data = data[data[asset_col] == asset]

            # Performance degradation analysis
            degradation = self._analyze_performance_degradation(asset_data, performance_cols)

            # Failure prediction
            failure_risk = self._predict_failure_risk(asset_data, performance_cols)

            # Maintenance recommendations
            maintenance_rec = self._generate_maintenance_recommendations(degradation, failure_risk)

            maintenance_insights[asset] = {
                'degradation_analysis': degradation,
                'failure_risk': failure_risk,
                'recommendations': maintenance_rec
            }

        return maintenance_insights

    def natural_language_insights(self, data: pd.DataFrame, query: str) -> Dict:
        """Process natural language queries about data"""
        query_lower = query.lower()

        # Simple NLP processing (can be enhanced with proper NLP libraries)
        insights = []

        # Revenue queries
        if 'revenue' in query_lower:
            if 'trend' in query_lower or 'growing' in query_lower:
                revenue_trend = self._analyze_trend(data['Revenue']) if 'Revenue' in data.columns else None
                if revenue_trend:
                    insights.append(f"Revenue shows {revenue_trend['direction']} trend with {revenue_trend['strength']} strength")

        # Prediction queries
        if 'predict' in query_lower or 'forecast' in query_lower:
            kpi = self._extract_kpi_from_query(query_lower, data.columns)
            if kpi:
                pred_result = self.predict_kpi(data, kpi, 3)
                if 'predictions' in pred_result:
                    insights.append(f"Predicted {kpi} for next 3 periods: {pred_result['predictions'][:3]}")

        # Anomaly queries
        if 'anomal' in query_lower or 'unusual' in query_lower:
            kpi = self._extract_kpi_from_query(query_lower, data.columns)
            if kpi:
                anomaly_result = self.detect_anomalies(data, kpi)
                if 'anomalies' in anomaly_result and anomaly_result['anomalies']:
                    insights.append(f"Found {len(anomaly_result['anomalies'])} anomalies in {kpi}")

        return {
            'query': query,
            'insights': insights,
            'confidence': 0.75,
            'suggestions': self._generate_query_suggestions(query_lower, data.columns)
        }

    # Helper methods
    def _analyze_trend(self, values: pd.Series) -> Dict:
        """Analyze trend in time series data"""
        if len(values) < 3:
            return {'direction': 'unknown', 'strength': 'low', 'confidence': 0.0}

        # Simple linear regression for trend
        x = np.arange(len(values))
        slope = np.polyfit(x, values, 1)[0]

        # Determine direction and strength
        if abs(slope) < values.std() * 0.1:
            direction = 'stable'
            strength = 'low'
        elif slope > 0:
            direction = 'upward'
            strength = 'high' if abs(slope) > values.std() * 0.5 else 'medium'
        else:
            direction = 'downward'
            strength = 'high' if abs(slope) > values.std() * 0.5 else 'medium'

        # Calculate confidence based on R²
        r_squared = np.corrcoef(x, values)[0, 1] ** 2 if len(values) > 1 else 0
        confidence = min(0.95, max(0.1, r_squared))

        return {
            'direction': direction,
            'strength': strength,
            'confidence': confidence,
            'slope': slope
        }

    def _analyze_volatility(self, values: pd.Series) -> Dict:
        """Analyze volatility in data"""
        std_dev = values.std()
        mean_val = values.mean()
        cv = std_dev / mean_val if mean_val != 0 else float('inf')

        if cv < 0.1:
            level = 'low'
        elif cv < 0.3:
            level = 'medium'
        else:
            level = 'high'

        return {
            'level': level,
            'std': std_dev,
            'coefficient_of_variation': cv
        }

    def _get_benchmark(self, kpi: str) -> Optional[float]:
        """Get industry benchmark for KPI"""
        benchmarks = {
            'Revenue': 1000000,
            'GP_Margin': 25.0,
            'Customer_Satisfaction': 85.0,
            'Conversion_Rate': 3.5,
            'Active_Users': 8000
        }
        return benchmarks.get(kpi)

    def _compare_to_benchmark(self, value: float, benchmark: float) -> Dict:
        """Compare value to benchmark"""
        difference = ((value - benchmark) / benchmark) * 100

        if difference > 10:
            status = 'significantly above'
            recommendation = 'Maintain current performance and identify success factors'
        elif difference > 0:
            status = 'above'
            recommendation = 'Good performance, look for optimization opportunities'
        elif difference > -10:
            status = 'slightly below'
            recommendation = 'Focus on improvement initiatives'
        else:
            status = 'significantly below'
            recommendation = 'Immediate action required to improve performance'

        return {
            'status': status,
            'difference': difference,
            'recommendation': recommendation
        }

    def _linear_prediction(self, values: pd.Series, periods: int) -> List[float]:
        """Simple linear regression prediction"""
        if not ML_AVAILABLE:
            return [values.iloc[-1] * 1.05] * periods

        X = np.arange(len(values)).reshape(-1, 1)
        y = values.values

        model = LinearRegression()
        model.fit(X, y)

        future_X = np.arange(len(values), len(values) + periods).reshape(-1, 1)
        predictions = model.predict(future_X)

        return predictions.tolist()

    def _simple_arima_prediction(self, values: pd.Series, periods: int) -> List[float]:
        """Simple ARIMA-like prediction"""
        # Simple exponential smoothing
        alpha = 0.3
        smoothed = [values.iloc[0]]

        for i in range(1, len(values)):
            smoothed.append(alpha * values.iloc[i] + (1 - alpha) * smoothed[-1])

        # Predict future values
        predictions = []
        last_smoothed = smoothed[-1]

        for _ in range(periods):
            predictions.append(last_smoothed)

        return predictions

    def _prophet_prediction(self, data: pd.DataFrame, kpi: str, periods: int) -> List[float]:
        """Prophet-based prediction"""
        if not PROPHET_AVAILABLE:
            return self._simple_arima_prediction(data[kpi], periods)

        try:
            # Prepare data for Prophet
            prophet_data = pd.DataFrame({
                'ds': data['Date'],
                'y': data[kpi]
            }).dropna()

            model = Prophet(daily_seasonality=False, weekly_seasonality=False)
            model.fit(prophet_data)

            # Make future predictions
            future = model.make_future_dataframe(periods=periods, freq='M')
            forecast = model.predict(future)

            return forecast['yhat'].tail(periods).tolist()
        except:
            return self._simple_arima_prediction(data[kpi], periods)

    def _ensemble_prediction(self, predictions: Dict, periods: int) -> List[float]:
        """Combine multiple predictions using ensemble method"""
        if not predictions:
            return [0] * periods

        # Simple average ensemble
        ensemble = []
        for i in range(periods):
            period_predictions = []
            for method, pred_list in predictions.items():
                if i < len(pred_list):
                    period_predictions.append(pred_list[i])

            if period_predictions:
                ensemble.append(np.mean(period_predictions))
            else:
                ensemble.append(0)

        return ensemble

    def _calculate_confidence_intervals(self, predictions: Dict, periods: int) -> Dict:
        """Calculate confidence intervals for predictions"""
        confidence_intervals = {}

        for method, pred_list in predictions.items():
            if len(pred_list) >= periods:
                # Simple confidence interval based on standard deviation
                std_dev = np.std(pred_list[:periods])
                lower_bound = [p - 1.96 * std_dev for p in pred_list[:periods]]
                upper_bound = [p + 1.96 * std_dev for p in pred_list[:periods]]

                confidence_intervals[method] = {
                    'lower': lower_bound,
                    'upper': upper_bound
                }

        return confidence_intervals

    def _evaluate_models(self, predictions: Dict, actual_values: pd.Series) -> Dict:
        """Evaluate prediction model performance"""
        if not ML_AVAILABLE or len(actual_values) < 10:
            return {}

        # Use last 20% of data for evaluation
        test_size = max(2, int(len(actual_values) * 0.2))
        train_data = actual_values[:-test_size]
        test_data = actual_values[-test_size:]

        performance = {}

        for method in predictions.keys():
            try:
                # Generate predictions for test period
                if method == 'linear':
                    test_predictions = self._linear_prediction(train_data, test_size)
                else:
                    test_predictions = self._simple_arima_prediction(train_data, test_size)

                # Calculate metrics
                mae = mean_absolute_error(test_data, test_predictions[:len(test_data)])
                mape = np.mean(np.abs((test_data - test_predictions[:len(test_data)]) / test_data)) * 100

                performance[method] = {
                    'mae': mae,
                    'mape': mape,
                    'accuracy': max(0, 100 - mape)
                }
            except:
                performance[method] = {'mae': 0, 'mape': 100, 'accuracy': 0}

        return performance

    def _generate_prediction_recommendations(self, predictions: List[float], historical: pd.Series) -> List[str]:
        """Generate recommendations based on predictions"""
        recommendations = []

        if not predictions or len(predictions) == 0:
            return recommendations

        current_value = historical.iloc[-1]
        predicted_value = predictions[0]

        change_percent = ((predicted_value - current_value) / current_value) * 100

        if change_percent > 10:
            recommendations.append(f"Strong growth predicted ({change_percent:.1f}%) - prepare for scaling")
        elif change_percent > 0:
            recommendations.append(f"Moderate growth expected ({change_percent:.1f}%) - maintain current strategy")
        elif change_percent > -10:
            recommendations.append(f"Slight decline predicted ({change_percent:.1f}%) - monitor closely")
        else:
            recommendations.append(f"Significant decline predicted ({change_percent:.1f}%) - immediate action needed")

        return recommendations

    def _isolation_forest_anomalies(self, values: pd.Series) -> List[int]:
        """Detect anomalies using Isolation Forest"""
        try:
            data_array = values.values.reshape(-1, 1)
            iso_forest = IsolationForest(contamination=0.1, random_state=42)
            anomalies = iso_forest.fit_predict(data_array)
            return [i for i, val in enumerate(anomalies) if val == -1]
        except:
            return []

    def _statistical_anomalies(self, values: pd.Series) -> List[int]:
        """Detect anomalies using statistical methods (Z-score)"""
        z_scores = np.abs((values - values.mean()) / values.std())
        return [i for i, z in enumerate(z_scores) if z > self.anomaly_threshold]

    def _seasonal_anomalies(self, values: pd.Series) -> List[int]:
        """Detect seasonal anomalies"""
        if len(values) < 24:  # Need at least 2 years of monthly data
            return []

        # Simple seasonal decomposition
        seasonal_period = 12
        seasonal_means = []

        for i in range(seasonal_period):
            seasonal_values = [values.iloc[j] for j in range(i, len(values), seasonal_period)]
            seasonal_means.append(np.mean(seasonal_values))

        anomalies = []
        for i, value in enumerate(values):
            seasonal_idx = i % seasonal_period
            expected = seasonal_means[seasonal_idx]

            if abs(value - expected) > 2 * np.std(values):
                anomalies.append(i)

        return anomalies

    def _combine_anomaly_results(self, anomalies: Dict, values: pd.Series) -> List[Dict]:
        """Combine anomaly detection results"""
        combined = {}

        for method, indices in anomalies.items():
            for idx in indices:
                if idx not in combined:
                    combined[idx] = {
                        'index': idx,
                        'value': values.iloc[idx],
                        'methods': [],
                        'severity': 0
                    }
                combined[idx]['methods'].append(method)
                combined[idx]['severity'] += 1

        return list(combined.values())

    def _assess_anomaly_severity(self, anomalies: List[Dict], values: pd.Series) -> Dict:
        """Assess overall anomaly severity"""
        if not anomalies:
            return {'level': 'none', 'count': 0, 'impact': 'minimal'}

        high_severity = sum(1 for a in anomalies if a['severity'] >= 2)
        total_anomalies = len(anomalies)

        if high_severity > total_anomalies * 0.5:
            level = 'high'
            impact = 'significant'
        elif total_anomalies > len(values) * 0.1:
            level = 'medium'
            impact = 'moderate'
        else:
            level = 'low'
            impact = 'minimal'

        return {
            'level': level,
            'count': total_anomalies,
            'high_severity_count': high_severity,
            'impact': impact
        }

    def _explain_anomalies(self, anomalies: List[Dict], values: pd.Series) -> List[str]:
        """Generate explanations for detected anomalies"""
        explanations = []

        for anomaly in anomalies:
            idx = anomaly['index']
            value = anomaly['value']
            methods = anomaly['methods']

            explanation = f"Anomaly at position {idx}: value {value:.2f} detected by {', '.join(methods)}"

            # Add context
            mean_val = values.mean()
            if value > mean_val * 1.5:
                explanation += " (unusually high)"
            elif value < mean_val * 0.5:
                explanation += " (unusually low)"

            explanations.append(explanation)

        return explanations

    def _anomaly_recommendations(self, anomalies: List[Dict]) -> List[str]:
        """Generate recommendations for handling anomalies"""
        if not anomalies:
            return ["No anomalies detected - data appears normal"]

        recommendations = []

        high_severity = sum(1 for a in anomalies if a['severity'] >= 2)

        if high_severity > 0:
            recommendations.append("High-severity anomalies detected - investigate root causes immediately")

        if len(anomalies) > 5:
            recommendations.append("Multiple anomalies detected - review data collection process")

        recommendations.append("Monitor these periods closely for recurring patterns")
        recommendations.append("Consider implementing automated alerts for similar anomalies")

        return recommendations

    def _get_trend_action(self, trend: Dict, kpi: str) -> str:
        """Get recommended action based on trend analysis"""
        direction = trend['direction']
        strength = trend['strength']

        if direction == 'upward' and strength == 'high':
            return f"Excellent {kpi} growth - maintain current strategies"
        elif direction == 'upward':
            return f"Positive {kpi} trend - consider scaling successful initiatives"
        elif direction == 'downward' and strength == 'high':
            return f"Concerning {kpi} decline - immediate intervention required"
        elif direction == 'downward':
            return f"Declining {kpi} trend - investigate causes and implement corrective measures"
        else:
            return f"Stable {kpi} - look for optimization opportunities"

    def _extract_kpi_from_query(self, query: str, columns: List[str]) -> Optional[str]:
        """Extract KPI name from natural language query"""
        query_words = query.lower().split()

        for col in columns:
            if col.lower() in query or any(word in col.lower() for word in query_words):
                return col

        # Common KPI mappings
        kpi_mappings = {
            'revenue': 'Revenue',
            'sales': 'Revenue',
            'margin': 'GP_Margin',
            'satisfaction': 'Customer_Satisfaction',
            'users': 'Active_Users',
            'conversion': 'Conversion_Rate'
        }

        for word in query_words:
            if word in kpi_mappings and kpi_mappings[word] in columns:
                return kpi_mappings[word]

        return None

    def _generate_query_suggestions(self, query: str, columns: List[str]) -> List[str]:
        """Generate query suggestions"""
        suggestions = [
            "Show me revenue trends for the last 6 months",
            "What's the correlation between customer satisfaction and revenue?",
            "Predict next quarter's performance",
            "Find anomalies in our data",
            "How is our GP margin performing?"
        ]

        # Add column-specific suggestions
        for col in columns:
            if 'Revenue' in col:
                suggestions.append(f"Analyze {col} growth patterns")
            elif 'Customer' in col:
                suggestions.append(f"What affects {col}?")

        return suggestions[:5]  # Return top 5 suggestions
